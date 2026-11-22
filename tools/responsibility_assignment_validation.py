"""DataCraft v0.0.1 ResponsibilityAssignment validation against repository model files."""
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import yaml

ASSIGNMENT_STATUS = {"ACTIVE", "INACTIVE", "SUPERSEDED"}
REQUIRED = {
    "handle", "scope", "responsibility", "responsible_role", "accountable_role",
    "consulted_roles", "informed_roles", "assignment_status", "provenance",
}


def load_yaml(path):
    with Path(path).open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_repository_model(repo_root):
    root = Path(repo_root)
    model_dir = root / "model"
    roles_doc = load_yaml(model_dir / "responsibility-roles.yaml")
    assignments_doc = load_yaml(model_dir / "responsibility-assignments.yaml")
    role_registry = set((roles_doc.get("responsibility_roles") or {}).keys())
    assignments = assignments_doc.get("responsibility_assignments") or []

    project_registry = set()
    profile_registry = set()
    product_registry = set()
    provider_registry = set()
    path_index = set()

    def walk(node):
        if isinstance(node, dict):
            handle = node.get("handle")
            object_type = str(node.get("type") or node.get("kind") or "").upper()
            if isinstance(handle, str):
                if handle.startswith("PROJECT-") or object_type == "PROJECT": project_registry.add(handle)
                if handle.startswith("PROFILE-") or object_type == "PROFILE": profile_registry.add(handle)
                if handle.startswith(("ENG-", "ADP-", "CON-", "PRT-", "BRIDGE-")): provider_registry.add(handle)
            for key in ("product", "software", "provider_name"):
                if isinstance(node.get(key), str): product_registry.add(node[key])
            if isinstance(node.get("path"), str): path_index.add(node["path"])
            for value in node.values(): walk(value)
        elif isinstance(node, list):
            for value in node: walk(value)

    for path in model_dir.rglob("*.yaml"):
        try: walk(load_yaml(path))
        except Exception: pass
    for path in model_dir.rglob("*.yml"):
        try: walk(load_yaml(path))
        except Exception: pass

    return {
        "role_registry": role_registry,
        "assignments": assignments,
        "project_registry": project_registry,
        "profile_registry": profile_registry,
        "product_registry": product_registry,
        "provider_registry": provider_registry,
        "path_index": path_index,
    }


def validate_l1(a, role_registry):
    errors = []
    missing = sorted(REQUIRED - set(a))
    if missing: errors.append(f"missing:{','.join(missing)}")
    for key in REQUIRED & set(a):
        if key in {"consulted_roles", "informed_roles"}: continue
        if not isinstance(a[key], str) or not a[key].strip(): errors.append(f"non_empty_string:{key}")
    for key in ("consulted_roles", "informed_roles"):
        if key not in a: continue
        if not isinstance(a[key], list):
            errors.append(f"list:{key}"); continue
        if len(a[key]) != len(set(a[key])): errors.append(f"unique:{key}")
        if set(a[key]) - role_registry: errors.append(f"unknown_role:{key}")
    if a.get("responsible_role") not in role_registry: errors.append("unknown_role:responsible_role")
    if a.get("accountable_role") not in role_registry: errors.append("unknown_role:accountable_role")
    if a.get("assignment_status") not in ASSIGNMENT_STATUS: errors.append("enum:assignment_status")
    if "project" in a and a["project"] is not None and (not isinstance(a["project"], str) or not a["project"].strip()):
        errors.append("project:syntax")
    return sorted(set(errors))


def is_project_scoped(scope): return scope == "project" or scope.startswith("project.")


def validate_l2(a, registries):
    errors = []
    assignments = registries["assignments"]
    if sum(x.get("handle") == a.get("handle") for x in assignments) != 1: errors.append("handle:not_unique")
    for field in ("responsible_role", "accountable_role"):
        if a.get(field) not in registries["role_registry"]: errors.append(f"role:not_resolvable:{field}")
    for field in ("consulted_roles", "informed_roles"):
        for role in a.get(field, []):
            if role not in registries["role_registry"]: errors.append(f"role:not_resolvable:{field}")
    if is_project_scoped(a.get("scope", "")):
        if not a.get("project"): errors.append("project:required_for_project_scope")
        elif a["project"] not in registries["project_registry"]: errors.append("project:not_resolvable")
    value = a.get("responsibility")
    forbidden_values = set().union(registries["profile_registry"], registries["product_registry"], registries["provider_registry"], registries["path_index"])
    if value in forbidden_values: errors.append("responsibility:implicit_from_profile_product_provider_or_path")
    if {"authority", "permission", "approval", "runtime_authorized"} & set(a):
        errors.append("responsibility_assignment:forbidden_governance_grant")
    return sorted(set(errors))


class PolicyDecision(str, Enum):
    ALLOW_AUTO="ALLOW_AUTO"; REQUIRE_APPROVAL="REQUIRE_APPROVAL"; DRY_RUN_ONLY="DRY_RUN_ONLY"; DENY="DENY"

@dataclass(frozen=True)
class RuntimeAuthorization:
    execution_allowed: bool
    side_effect_allowed: bool
    reason: str


def evaluate_runtime_authorization(*, assignment_valid, permission, authority_required, authority_satisfied,
                                   policy_decision, approval=False, state_valid=True, budget_available=True,
                                   provider_available=True):
    try: decision = PolicyDecision(policy_decision)
    except ValueError: return RuntimeAuthorization(False, False, "UNKNOWN_POLICY_DECISION")
    if not assignment_valid: return RuntimeAuthorization(False, False, "INVALID_ASSIGNMENT")
    if not permission: return RuntimeAuthorization(False, False, "MISSING_PERMISSION")
    if authority_required and not authority_satisfied: return RuntimeAuthorization(False, False, "MISSING_AUTHORITY")
    if not state_valid: return RuntimeAuthorization(False, False, "INVALID_STATE")
    if not budget_available: return RuntimeAuthorization(False, False, "BUDGET_EXCEEDED")
    if not provider_available: return RuntimeAuthorization(False, False, "PROVIDER_UNAVAILABLE")
    if decision is PolicyDecision.DENY: return RuntimeAuthorization(False, False, "POLICY_DENY")
    if decision is PolicyDecision.DRY_RUN_ONLY: return RuntimeAuthorization(True, False, "DRY_RUN_ONLY")
    if decision is PolicyDecision.REQUIRE_APPROVAL and not approval: return RuntimeAuthorization(False, False, "APPROVAL_REQUIRED")
    return RuntimeAuthorization(True, True, "AUTHORIZED")
