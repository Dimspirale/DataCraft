import unittest
from pathlib import Path
from tools.responsibility_assignment_validation import (
    load_repository_model, validate_l1, validate_l2, evaluate_runtime_authorization
)

BASE = {
    "handle": "RA-MODEL-001", "scope": "model.canonical",
    "responsibility": "maintain_canonical_model",
    "responsible_role": "MODEL_OWNER", "accountable_role": "MODEL_OWNER",
    "consulted_roles": ["GOVERNANCE_OWNER"], "informed_roles": ["PROJECT_OWNER"],
    "project": None, "assignment_status": "ACTIVE", "provenance": "ARCH",
}

REPO_ROOT = Path(__file__).resolve().parents[1]
REG = load_repository_model(REPO_ROOT)
ROLE_SET = REG["role_registry"]

class L1Tests(unittest.TestCase):
    def test_01_valid_minimal(self): self.assertEqual([], validate_l1(dict(BASE), ROLE_SET))
    def test_02_missing_required_field(self):
        a=dict(BASE); del a["handle"]; self.assertTrue(any(x.startswith("missing:") for x in validate_l1(a, ROLE_SET)))
    def test_03_scope_required(self):
        a=dict(BASE); a["scope"]=""; self.assertIn("non_empty_string:scope",validate_l1(a, ROLE_SET))
    def test_04_responsibility_required(self):
        a=dict(BASE); a["responsibility"]=""; self.assertIn("non_empty_string:responsibility",validate_l1(a, ROLE_SET))
    def test_05_unknown_responsible_rejected(self):
        a=dict(BASE); a["responsible_role"]="AGENT_CAD"; self.assertIn("unknown_role:responsible_role",validate_l1(a, ROLE_SET))
    def test_06_unknown_accountable_rejected(self):
        a=dict(BASE); a["accountable_role"]="AGENT_CAD"; self.assertIn("unknown_role:accountable_role",validate_l1(a, ROLE_SET))
    def test_07_consulted_must_be_list(self):
        a=dict(BASE); a["consulted_roles"]="MODEL_OWNER"; self.assertIn("list:consulted_roles",validate_l1(a, ROLE_SET))
    def test_08_consulted_unique(self):
        a=dict(BASE); a["consulted_roles"]=["MODEL_OWNER","MODEL_OWNER"]; self.assertIn("unique:consulted_roles",validate_l1(a, ROLE_SET))
    def test_09_informed_unique(self):
        a=dict(BASE); a["informed_roles"]=["PROJECT_OWNER","PROJECT_OWNER"]; self.assertIn("unique:informed_roles",validate_l1(a, ROLE_SET))
    def test_10_status_and_project_syntax(self):
        a=dict(BASE); a["assignment_status"]="SUPPORTED"; a["project"]=42
        e=validate_l1(a, ROLE_SET); self.assertIn("enum:assignment_status",e); self.assertIn("project:syntax",e)

class L2Tests(unittest.TestCase):
    def check(self,a,assignments=None):
        original = REG["assignments"]
        REG["assignments"] = assignments or [a]
        try:
            return validate_l2(a, REG)
        finally:
            REG["assignments"] = original

    def test_11_repository_assignments_are_valid(self):
        self.assertTrue(REG["assignments"], "repository model must define assignments")
        for assignment in REG["assignments"]:
            self.assertEqual([], validate_l1(assignment, ROLE_SET), assignment.get("handle"))
            self.assertEqual([], validate_l2(assignment, REG), assignment.get("handle"))
    def test_12_duplicate_handle(self):
        a=dict(BASE); self.assertIn("handle:not_unique",self.check(a,[a,dict(a)]))
    def test_13_project_required_for_project_scope(self):
        a=dict(BASE); a["scope"]="project.rigging"; self.assertIn("project:required_for_project_scope",self.check(a))
    def test_14_project_must_resolve(self):
        a=dict(BASE); a.update(scope="project.rigging",project="PROJECT-NOT-FOUND"); self.assertIn("project:not_resolvable",self.check(a))
    def test_15_valid_project_scope(self):
        if not REG["project_registry"]:
            self.skipTest(
                "No PROJECT exists in the repository model yet."
            )

        project = sorted(REG["project_registry"])[0]

        a = dict(BASE)
        a.update(
            scope="project.validation",
            project=project,
        )

        self.assertEqual([], self.check(a))
    def test_16_role_must_resolve_through_registry(self):
        a=dict(BASE); a["responsible_role"]="UNKNOWN_OWNER"; self.assertIn("role:not_resolvable:responsible_role",self.check(a))
    def test_17_profile_not_inferred(self):
        a=dict(BASE); a["responsibility"]="Rigger"; REG["profile_registry"].add("Rigger")
        try: self.assertIn("responsibility:implicit_from_profile_product_provider_or_path",self.check(a))
        finally: REG["profile_registry"].discard("Rigger")
    def test_18_product_not_inferred(self):
        a=dict(BASE); a["responsibility"]="Ollama"; REG["product_registry"].add("Ollama")
        try: self.assertIn("responsibility:implicit_from_profile_product_provider_or_path",self.check(a))
        finally: REG["product_registry"].discard("Ollama")
    def test_19_provider_not_inferred(self):
        a=dict(BASE); a["responsibility"]="ENG-Qdrant"; REG["provider_registry"].add("ENG-Qdrant")
        try: self.assertIn("responsibility:implicit_from_profile_product_provider_or_path",self.check(a))
        finally: REG["provider_registry"].discard("ENG-Qdrant")
    def test_20_path_not_inferred(self):
        value=r"C:\Users\dimit\OneDrive\DataCraft"; a=dict(BASE); a["responsibility"]=value; REG["path_index"].add(value)
        try: self.assertIn("responsibility:implicit_from_profile_product_provider_or_path",self.check(a))
        finally: REG["path_index"].discard(value)
    def test_21_assignment_cannot_grant_authority_permission_approval(self):
        for field in ("authority","permission","approval","runtime_authorized"):
            a=dict(BASE); a[field]=True
            self.assertIn("responsibility_assignment:forbidden_governance_grant",self.check(a))

class L3Tests(unittest.TestCase):
    def auth(self,**kw):
        defaults=dict(assignment_valid=True,permission=True,authority_required=False,
                      authority_satisfied=False,policy_decision="ALLOW_AUTO",approval=False,
                      state_valid=True,budget_available=True,provider_available=True)
        defaults.update(kw); return evaluate_runtime_authorization(**defaults)
    def test_22_assignment_alone_does_not_authorize(self):
        self.assertFalse(self.auth(permission=False).execution_allowed)
    def test_23_unknown_policy_fails_closed(self):
        self.assertEqual("UNKNOWN_POLICY_DECISION",self.auth(policy_decision="UNKNOWN").reason)
    def test_24_policy_deny_wins(self):
        self.assertFalse(self.auth(policy_decision="DENY").execution_allowed)
    def test_25_dry_run_allows_execution_not_side_effect(self):
        r=self.auth(policy_decision="DRY_RUN_ONLY"); self.assertTrue(r.execution_allowed); self.assertFalse(r.side_effect_allowed)
    def test_26_approval_required(self):
        self.assertFalse(self.auth(policy_decision="REQUIRE_APPROVAL").execution_allowed)
        self.assertTrue(self.auth(policy_decision="REQUIRE_APPROVAL",approval=True).side_effect_allowed)
    def test_27_authority_required_only_when_applicable(self):
        self.assertTrue(self.auth(authority_required=False,authority_satisfied=False).side_effect_allowed)
        self.assertFalse(self.auth(authority_required=True,authority_satisfied=False).execution_allowed)
    def test_28_invalid_state_blocks(self): self.assertEqual("INVALID_STATE",self.auth(state_valid=False).reason)
    def test_29_budget_blocks(self): self.assertEqual("BUDGET_EXCEEDED",self.auth(budget_available=False).reason)
    def test_30_provider_unavailable_blocks(self): self.assertEqual("PROVIDER_UNAVAILABLE",self.auth(provider_available=False).reason)

if __name__ == "__main__": unittest.main()
