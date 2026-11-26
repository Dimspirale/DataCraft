# ADR-0002 - Minimum Useful Evaluation Harness

Status: ACCEPTED
Date: 2026-11-25
Scope: DataCraft v0.0.1

## Context

DataCraft needs a repeatable way to determine whether a change improves or regresses a real use case without making evaluation agent-centric or introducing a new Core primitive.

The canonical responsibility chain remains unchanged:

`PROJECT -> PROFILE -> CAPABILITY -> SKILL -> POLICY -> RESOLVER -> EXECUTION -> RUN -> RESULT -> EVIDENCE`

Evaluation is a capability/skill applied to an explicit target. It does not become a new step in the canonical chain.

## Decision

For v0.0.1, DataCraft adopts a **Minimum Useful Evaluation Harness** attached to the first real business use case.

The first implementation should contain only:

1. a small set of representative evaluation scenarios/fixtures;
2. explicit success criteria;
3. deterministic graders wherever the requirement is deterministically checkable;
4. persisted RUN and RESULT data sufficient for comparison;
5. EVIDENCE supporting the evaluation claim;
6. a baseline/candidate comparison when evaluating a change;
7. regression cases derived from qualified real-world EVIDENCE when relevant.

Evaluation orchestration reuses existing EXECUTION/RUN responsibilities, including bounded budgets, RETRY semantics, pause/resume constraints and observability where required.

## Invariants

- `Evaluation Target != Agent`
- `Evaluation Definition != Evaluation RUN != Evaluation RESULT`
- `Changed Grader != Comparable Evaluation`
- `Better Score != Better System`
- `Resumable RUN != Valid Resume Under Changed Conditions`
- `Evaluation Success != Production Fitness`
- `Unified Evaluation Framework != Universal Evaluator`

Existing invariants remain applicable, including:

- `RESULT != EVIDENCE`
- `Observation != Evaluation`
- `Evaluation != Policy`
- `LLM Evaluation != Ground Truth`
- `Automated Test Passed != Requirement Satisfied`
- `DRY_RUN != SHADOW_MODE`
- `Deployment Authorization != Runtime Authorization`

## Remapping

- Agent evaluation -> evaluation of a CAPABILITY, SKILL or implementation candidate according to its actual responsibility.
- Fixture -> versioned evaluation scenario/artifact.
- Grader -> evaluation mechanism/implementation.
- Evaluation pipeline -> orchestration using existing EXECUTION and RUN responsibilities.
- Golden dataset -> versioned cases and expectations; never Knowledge by definition.
- Evaluation result store -> RESULT/EVIDENCE persistence according to responsibility.
- Shared model gateway -> existing Gateway/Provider abstraction.

## Grading policy

Prefer the cheapest trustworthy evaluation mechanism appropriate to the requirement:

1. deterministic assertion/check when possible;
2. model-based evaluation only where interpretation is genuinely required;
3. human or domain Authority review when required by ambiguity, criticality or domain governance.

A model grader never becomes Ground Truth or Authority by virtue of grading.

## Resume and reproducibility

A paused evaluation may resume only when the material evaluation conditions remain compatible. Changes to the system under evaluation, fixture/scenario, grader, model configuration, provider behavior, tool exposure or other material conditions must not be silently treated as the same comparable RUN.

## Production boundary

Evaluation may execute the same implementation code as production where useful, but:

`Same Code != Same Runtime Conditions`

and

`Evaluation Success != Production Fitness`.

Promotion to controlled execution remains governed separately by POLICY and RuntimeAuthorized.

## v0.0.1 constraints

DEFER:

- universal evaluation platform;
- sophisticated evaluation dashboards;
- large golden datasets;
- multiple LLM judges by default;
- distributed evaluation infrastructure;
- automatic promotion to production;
- complex continuous evaluation.

REJECT:

- `EvaluatorAgent` as a Core primitive;
- Evaluation as a new Core responsibility;
- a single score as global quality or Authority;
- an LLM judge as Ground Truth;
- a better score as automatic proof of a better system;
- benchmark success as RuntimeAuthorized;
- evaluation success as deployment authorization;
- automatic conversion of production feedback into Knowledge.

## First-use loop

`REAL PROBLEM -> representative scenarios -> explicit criteria -> EXECUTION -> RUN -> RESULT -> EVALUATION -> EVIDENCE -> decision`

When a qualified real-world failure reveals a deterministically testable invariant, prefer adding a regression control/test rather than another prompt rule.

## Consequence

DataCraft gains a minimal mechanism for measurable improvement while keeping the Core unchanged and avoiding an agent-centric evaluation architecture.
