# DataCraft Copilot Instructions

## Scope

These instructions govern development assistance for DataCraft v0.0.1.
DataCraft is model-centric. Development tools assist construction; they are not the DataCraft runtime, the canonical model, or automatic business Authority.

## Current construction focus

Current stream: `BUILD-00 — Canonical Foundation`.

Prioritize:

1. `DC-001` — canonical model;
2. `DC-002` — canonical identity.

Do not introduce infrastructure or abstractions merely because they may be useful later. Prefer the smallest portable implementation that tests the current hypothesis.

## Canonical responsibility chain

`PROJECT -> PROFILE -> CAPABILITY -> SKILL -> POLICY -> RESOLVER -> EXECUTION -> RUN -> RESULT -> EVIDENCE`

This is a chain of applicable responsibilities, not a mandatory physical pipeline that must materialize every object for every operation.

## Core invariants

Preserve these distinctions:

- `PROFILE != Agent`
- `CAPABILITY != software`
- `SKILL != script`
- `POLICY != standard`
- `Knowledge != Memory`
- `Memory != State`
- `State != Policy`
- `Knowledge != Policy`
- `RESULT != EVIDENCE`
- `Evidence != Memory`
- `Authority != Permission`
- `Approval != Authority`
- `Provenance != Authority`
- `Criticality != OperationalImpact`
- `Phase != Status`
- `Phase != SupportStatus`
- `Handle != ID`
- `ID != Alias`
- `Handle != Path`
- `Path != identity`
- `Path != permission`
- `Path != phase`
- `Provider != Capability`
- `ENG != Core`
- `Development Tool != Runtime`
- `Installed != Integrated`
- `Integrated != Validated`
- `Validated != Supported`
- `UNKNOWN != SUPPORTED`
- `Import != Merge != Sync`
- `Resource != Definition != Instance`
- `Geometry != Topology != Semantics`
- `Backup != Replication != Redundancy`
- `Failover != Failback`
- `DataCraft != automatic business Authority`

Legacy families `SYS`, `DS`, `DM`, `AG`, `MD`, and `IA` may occur in migration or historical resources, but MUST NOT be introduced as active canonical object types.

## Identity

Use these meanings:

- `Handle`: immutable internal identity;
- `ID`: canonical human-readable identifier;
- `Alias`: legacy identifier only for a genuine 1:1 correspondence;
- `Path`: mutable location;
- `ExternalIdentity`: identity in an external system.

A Path change MUST NOT change identity.
If one legacy object becomes multiple new objects, use an explicit, auditable `MIG`. Do not use Alias for 1:N transformations.

## Authority and safety

DataCraft, Copilot, generic code, and LLM outputs are not automatic business Authority.
A specialized engine may be Authority only for an explicitly assigned scope, object type, or property.

Keep separate:

- Authority — what makes a value authoritative;
- Permission — what may act;
- POLICY — under which conditions an action is allowed;
- Approval — who or what accepts a specific action.

Any new side-effecting action MUST satisfy POLICY before EXECUTION.
Do not silently expand permissions, scopes, budgets, retries, iteration limits, or execution limits.

Never place secrets or tokens in repository files, prompts, logs, test fixtures, or Evidence. Use `SecretRef` when the relevant build stage introduces it.

## Execution discipline

Prefer explicit bounded execution properties when they become applicable:

- timeout;
- retry policy;
- max attempts;
- max steps;
- budget;
- dry-run;
- cancellation;
- idempotency;
- failure mode.

`RETRY != REPLAN`.
A replanned side-effecting action must return through POLICY before execution.
No agentic loop may silently extend its own limits or modify its own POLICY.

## Validation discipline

Always distinguish:

- L1 — Schema Validation;
- L2 — Model Validation;
- L3 — Runtime Validation.

`SchemaValid != ModelValid != RuntimeAuthorized`.
A structural validation confers neither Permission nor Authority.

`RESULT != EVIDENCE`.
`IMPLEMENTED != VALIDATED`.
A backlog item MUST NOT be called VALIDATED until its applicable acceptance criteria and tests have passed and the required Evidence has been recorded.

For meaningful changes prefer:

`small change -> validation -> test -> commit -> use -> Evidence -> next decision`

## State, Memory, Knowledge, and Evidence

Keep these responsibilities distinct:

- State: what is true now for a scope;
- Memory: what DataCraft selectively retains from past experience;
- Knowledge: qualified, usable information;
- Policy: a rule governing a decision or execution;
- Evidence: retained support for what actually happened or for a governed conclusion.

A successful Result or LLM output MUST NOT automatically become Memory or Knowledge.

## Repository discipline

The repository tree is not the DataCraft ontology.
Do not derive type, identity, Authority, Permission, lifecycle, phase, or semantics from file paths.

Keep conceptually distinct:

- Definition;
- Implementation;
- Test;
- Evidence.

Registries, when introduced, MUST be governed views derived from the model, not second manually maintained sources of truth.

Do not recreate a universal ChangeLog. Keep ADR, MIG, RUN, Evidence, DocumentHistory, and Security/Audit events semantically distinct.

## Product and provider discipline

External products, frameworks, LLMs, IDEs, assistants, containers, databases, and orchestration frameworks remain replaceable implementations or development tools.
They MUST NOT become Core primitives merely because they are used.

Do not infer `SUPPORTED` from mention, discovery, installation, or integration.
Treat unknown status as `UNKNOWN` until Evidence supports a stronger status.

## Development tool discipline

VS Code, GitHub Copilot, GitLens, XML tooling, remote tooling, and similar utilities are Development Tools.
They may assist construction but are not DataCraft runtime components or business Authority.

Do not require Docker, Kubernetes, vector databases, RAG stacks, agent frameworks, or other infrastructure for BUILD-00 unless a validated dependency explicitly requires them.

## Working method

When proposing or modifying an abstraction:

1. identify the real need;
2. find the existing canonical responsibility that should own it;
3. verify invariants;
4. distinguish Core, Extension, Integration, and Implementation;
5. identify contradictions and unknowns explicitly;
6. prefer portable, reversible, minimal solutions;
7. define how the change will be tested;
8. identify the Evidence expected before calling the change validated.

Challenge previous decisions when new Evidence contradicts them. Do not preserve an old abstraction merely because it existed in historical DataCraft material.
