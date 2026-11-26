# ADR-0003 — Runtime agentique gouverné et indépendant des fournisseurs

Status: ACCEPTED
Date: 2026-11-25
Scope: Core + Runtime DataCraft

## Decision

DataCraft est **agentic-capable mais non agent-centric**.

La chaîne canonique reste inchangée :

`PROJECT -> PROFILE -> CAPABILITY -> SKILL -> POLICY -> RESOLVER -> EXECUTION -> RUN -> RESULT -> EVIDENCE`

Les comportements agentiques, SDK, runtimes, agents, handoffs, tools, protocoles et clouds fournisseurs sont des mécanismes d'Implementation/Integration/Provider. Ils ne deviennent pas des primitives Core.

## Cross-provider architecture review

La décision a été challengée à partir des orientations publiques de quatre écosystèmes :

- Anthropic : simple-first, context engineering, outils ciblés, harness, travail incrémental et evals.
- OpenAI : tools structurés, agent loop/runtime, guardrails, approvals, tracing, handoffs, sessions et evals.
- Microsoft : niveau minimal de complexité suffisant, identité/RBAC, isolation, observabilité, lifecycle, modèles interchangeables et patterns d'orchestration.
- Google : workflow agents, orchestration dynamique, spécialisation, multi-agent, A2A, évaluation des trajectoires et runtimes interchangeables.

Ces patterns sont utiles mais sont remappés vers les responsabilités DataCraft existantes.

## Complexity rule

Toujours préférer le mécanisme le plus simple satisfaisant fiablement le besoin :

1. DETERMINISTIC
2. boucle classique
3. workflow structuré
4. HYBRID
5. ALC
6. orchestration multi-agent spécialisée uniquement si une EVIDENCE démontre sa valeur.

## Controlled agentic loop

ALC = Agentic Loop Controlled.

`RESOLVE -> POLICY -> EXECUTE -> OBSERVE -> EVALUATE -> DISPOSE`

Dispositions : `COMPLETE`, `CONTINUE`, `RETRY`, `REPLAN`, `ESCALATE`, `ABORT`.

`RETRY != REPLAN`.

Toute nouvelle action à effet de bord issue d'un REPLAN repasse par POLICY.

## Context engineering

Le contexte modèle est dérivé et gouverné :

`Structured Brief -> Context Builder -> authorized context -> Model Input`

Le Context Builder peut sélectionner Knowledge, STATE, Memory qualifiée, sources, provenance, contraintes et instructions de SKILL selon le besoin.

`Prompt != Intent`.

`Model Input != Source Of Truth`.

`Present In Context != Stored != Remembered != Known != Validated`.

## Tools and integrations

Les tools fournisseurs sont remappés selon leur responsabilité réelle.

Une opération callable n'est pas une CAPABILITY et n'est pas automatiquement autorisée.

`Tool Callable != Tool Authorized`.

`CAPABILITY -> SKILL -> POLICY -> RESOLVER -> EXECUTION` reste la discipline DataCraft.

API, CLI, MCP, OSC, A2A et autres mécanismes sont des interfaces/protocoles interchangeables.

## Guardrails and POLICY

`Guardrail != POLICY`.

Un guardrail peut filtrer, valider, détecter ou bloquer techniquement. POLICY décide si une action est autorisée dans le contexte DataCraft en considérant notamment Identity, Permission, Authority, Approval, STATE, OperationalImpact, budgets et disponibilité des providers.

## Approval and resume

Une Approval porte sur une action concrète et ne confère pas une autorisation générale.

`Approved Action != Any Future Equivalent-Looking Action`.

La reprise après pause exige une réévaluation des conditions runtime pertinentes.

`Approval != Authority != Permission`.

`Resume != Retry != Replan`.

## Context, session, Memory and Knowledge

`Persistent Session Context != Memory`.

`Session Context != RUN State != Memory != Knowledge != STATE`.

Le pipeline d'apprentissage reste :

`RUN -> RESULT -> EVIDENCE -> Memory candidate -> qualification -> MEMORY -> Knowledge candidate -> validation/sourcing -> KNOWLEDGE`.

## Observability and EVIDENCE

`Log != Metric != Trace != Evidence`.

`Trace Complete != Evidence Sufficient`.

Tracing, logs et métriques contribuent potentiellement à une EVIDENCE, mais ne deviennent pas automatiquement une preuve suffisante.

## Evaluation

`Evaluation Target != Agent`.

Le Minimum Useful Evaluation Harness peut évaluer une CAPABILITY, SKILL, règle déterministe, Provider, RESOLVER, retrieval, modèle, ALC, intégration ou RESULT.

Préférer les graders déterministes lorsque possible. Les trajectoires peuvent être évaluées lorsqu'elles sont normatives, mais :

`Expected Trajectory != Only Valid Trajectory`.

## Cloud and provider boundaries

`Cloud Project != DataCraft PROJECT`.

`RBAC Permission != Business Authority`.

`Agent Type != DataCraft Responsibility`.

`Protocol Compatibility != Semantic Compatibility`.

Managed runtimes, Foundry, ADK, Agents SDKs, Claude Agent SDK, A2A, MCP, Cloud Run, GKE, Azure et autres stacks restent remplaçables.

## Multi-agent

Multi-agent est DEFER comme architecture générale.

Il peut devenir une Implementation d'une CAPABILITY si un besoin réel et une EVIDENCE démontrent un avantage suffisant par rapport à une solution plus simple.

`Orchestration Role != Agent Primitive`.

`Delegation != Authority Transfer`.

`Context Transfer != Permission Transfer`.

## Consequences for v0.0.1

Aucune nouvelle primitive Core.

Aucune nouvelle dépendance fournisseur obligatoire.

Priorité :

`real business problem -> minimal implementation -> validation -> controlled execution -> RUN -> RESULT -> EVIDENCE -> evaluation -> next decision`.

## External references

- Anthropic — Building effective agents; Effective context engineering; Writing effective tools; Demystifying evals.
- OpenAI — Practical guide to building agents; Agents SDK; guardrails, approvals, tracing and eval guidance.
- Microsoft — Azure Architecture Center agent orchestration patterns; Microsoft Foundry Agent Service.
- Google Cloud — ADK documentation; single-agent and multi-agent reference architectures.
