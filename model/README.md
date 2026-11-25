# DataCraft Model

Ce répertoire contient les Definitions canoniques indépendantes des moteurs externes.

Première Capability : `CAP.SECURITY.OS_CONFINEMENT`.

## Frontière du modèle

Le modèle décrit les responsabilités et invariants DataCraft ; il ne dépend pas de l'arborescence du dépôt ni d'un framework, provider, protocole ou produit particulier.

Chaîne canonique de responsabilité :

`PROJECT -> PROFILE -> CAPABILITY -> SKILL -> POLICY -> RESOLVER -> EXECUTION -> RUN -> RESULT -> EVIDENCE`

Séparations à préserver lors de l'évolution du modèle :

- `Definition != Instance`.
- `RESOURCE != STATE != CAPABILITY != PROVIDER`.
- `Interface != Protocol != Capability`.
- `Model-valid relationship != Observed relationship != Validated Knowledge`.
- `Semantic consistency != Factual truth`.
- `Result != Evidence != Memory != Knowledge`.
- `Dashboard != State != Evidence`.
- `Current Plan != Original Intent`.
- `Replan != Intent Mutation`.
- `Derived Goal != User Intent != Authorized Goal`.
- `State Persistence != Memory`.
- `Resume State != Remembered Experience`.
- `Planning != Retrieval`.
- `Reasoning Technique != Plan`.
- `Generated Plan != Authorized Plan`.
- `Autonomous Execution != Autonomous Authorization`.
- `Delegation != Authority Transfer`.
- `Learning Signal != Accepted Learning`.
- `Observed Success != Reusable Rule`.
- `Repeated Success != Knowledge`.
- `Self-Improvement != Self-Modification`.
- `Feedback != Learning`.
- `Evaluation != Memory`.
- `Rollback Available != Rollback Authorized`.
- `Recovery Action != Reversal Of History`.
- `More Agentic != More Advanced`.
- `More Autonomous != More Capable`.

Une relation permise par le modèle exprime ce qui est structurellement ou sémantiquement admissible. Elle ne constitue pas à elle seule une observation du réel ni une connaissance validée.

## Adaptation et préservation de l'intention

L'adaptation peut modifier la stratégie d'exécution ; elle ne peut jamais modifier silencieusement l'intention, l'Authority, la POLICY ou ce qui est considéré comme vrai.

Le Structured Brief porte l'intention structurée d'entrée. Un REPLAN retourne au RESOLVER mais ne réécrit pas implicitement cette intention. Un objectif dérivé reste une proposition de résolution et ne devient pas automatiquement un objectif autorisé.

Toute nouvelle action à effet de bord issue d'un REPLAN, d'une récupération, d'une compensation ou d'un rollback repasse par POLICY avant EXECUTION. Une action de récupération crée sa propre occurrence RUN et ne réécrit pas l'historique d'une exécution antérieure.

La persistance nécessaire à Pause/Resume relève de STATE tant qu'elle décrit l'exécution en cours. Elle ne devient pas automatiquement Memory. De même, feedback, évaluations et succès observés alimentent éventuellement EVIDENCE et des candidats à qualification ; ils ne modifient automatiquement ni Knowledge, ni POLICY, ni le Core.

Les technologies de stockage, vector databases, moteurs RAG, frameworks agentiques, protocoles A2A/MCP, API servers et providers d'observabilité restent des implémentations remplaçables introduites uniquement lorsqu'une CAPABILITY concrète le nécessite.

Multi-agent, autonomie longue durée, goal chaining avancé, dynamic tooling, marketplaces d'agents et self-learning runtime restent différés tant qu'un besoin concret et de l'EVIDENCE ne les justifient pas. `Agent`, `SelfImprovingAgent`, `AgentProtocol`, `AgentContract`, `AgentMemory`, `GoalChain` et `EvaluatorAgent` ne sont pas des primitives Core.
