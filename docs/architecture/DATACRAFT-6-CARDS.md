# DataCraft — Les 6 cartes de référence

Ce document est la légende textuelle canonique des six visuels pédagogiques DataCraft.

Les libellés français sont destinés à l'UX et aux explications. Les identifiants anglais restent canoniques dans le code et le modèle.

## Carte 1 — Le Cœur

Chaîne pédagogique :

**PROJET -> PROFIL -> CAPACITÉ -> SAVOIR-FAIRE -> POLITIQUE -> RÉSOLUTION -> ACTION -> ACTION RÉALISÉE -> RÉSULTAT -> PREUVE**

Chaîne canonique :

`PROJECT -> PROFILE -> CAPABILITY -> SKILL -> POLICY -> RESOLVER -> EXECUTION -> RUN -> RESULT -> EVIDENCE`

## Carte 2 — Le Runtime

Représente :

- canaux d'accès Desktop Dim, Laptop Dim, Mobile Dim et interfaces futures ;
- Structured Brief et Context Builder ;
- RESOLVER, POLICY, EXECUTION et OBSERVE ;
- MODEL, Provider, Gateway et Execution Backend interchangeables ;
- intégrations métier via API, CLI, MCP, OSC ou autres mécanismes ;
- RESOURCE et STATE distincts ;
- observabilité, guardrails, évaluations et budgets comme préoccupations transversales.

Principes :

`Provider != Capability`

`Resource != State`

`Interface != Protocol != Capability`

`Service Ready != CAPABILITY Available`

## Carte 3 — Le Comportement

Ordre de complexité privilégié :

`DETERMINISTIC -> classic loop -> structured workflow -> HYBRID -> ALC`

ALC :

`RESOLVE -> POLICY -> EXECUTE -> OBSERVE -> EVALUATE -> DISPOSE`

Dispositions : `COMPLETE`, `CONTINUE`, `RETRY`, `REPLAN`, `ESCALATE`, `ABORT`.

`RETRY != REPLAN`.

DataCraft utilise l'ALC seulement lorsqu'une adaptation réelle est nécessaire.

## Carte 4 — Information & Vérité

Séparations :

`SOURCE != KNOWLEDGE != MEMORY != STATE`.

Provenance :

`SOURCE ORIGINAL -> EXTRACT -> NORMALIZE -> VALIDATE -> DERIVED PROJECTION`.

Apprentissage :

`real event -> RUN -> RESULT -> EVIDENCE -> Memory candidate -> qualification -> MEMORY -> Knowledge candidate -> validation/sourcing -> KNOWLEDGE`.

Aucune sortie réussie ou échouée ne devient automatiquement Memory ou Knowledge.

## Carte 5 — Gouvernance & Validation

Trois validations distinctes :

`SchemaValid != ModelValid != RuntimeAuthorized`.

POLICY produit notamment :

- `ALLOW_AUTO`
- `REQUIRE_APPROVAL`
- `DRY_RUN_ONLY`
- `DENY`

Séparations :

`Identity != Authentication != Authorization`

`Authority != Permission != Approval`

`Criticality != OperationalImpact`

`Authenticated Identity != Authorized Action`

## Carte 6 — Construction & Amélioration

Boucle privilégiée :

`real business problem -> Structured Brief -> small change -> diff/review -> SchemaValid -> ModelValid -> tests -> commit -> real usage -> RUN -> RESULT -> EVIDENCE -> EVALUATION -> next decision`.

Parcours de promotion :

`prototype -> DRY_RUN -> SHADOW_MODE -> controlled execution -> EVIDENCE -> evaluation`.

Le dépôt Git est la référence versionnée du développement.

Le Minimum Useful Evaluation Harness utilise quelques scénarios représentatifs, des critères explicites et des graders déterministes autant que possible.

## Cross-provider decision

Anthropic, OpenAI, Microsoft et Google sont utilisés comme sources de patterns et de challenge architectural, jamais comme ontologie DataCraft.

DataCraft reste **agentic-capable but not agent-centric**.

Le mécanisme peut changer. La responsabilité reste stable.
