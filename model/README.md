# DataCraft Model

Ce répertoire contient les Definitions canoniques indépendantes des moteurs externes.

Première Capability : `CAP.SECURITY.OS_CONFINEMENT`.

## Frontière du modèle

Le modèle décrit les responsabilités et invariants DataCraft ; il ne dépend pas de l'arborescence du dépôt ni d'un framework, provider, protocole ou produit particulier.

Séparations à préserver lors de l'évolution du modèle :

- `Definition != Instance`.
- `RESOURCE != STATE != CAPABILITY != PROVIDER`.
- `Interface != Protocol != Capability`.
- `Model-valid relationship != Observed relationship != Validated Knowledge`.
- `Semantic consistency != Factual truth`.
- `Result != Evidence != Memory != Knowledge`.
- `Dashboard != State != Evidence`.

Une relation permise par le modèle exprime ce qui est structurellement ou sémantiquement admissible. Elle ne constitue pas à elle seule une observation du réel ni une connaissance validée.

Les technologies de stockage, vector databases, moteurs RAG, frameworks agentiques, API servers et providers d'observabilité restent des implémentations remplaçables introduites uniquement lorsqu'une CAPABILITY concrète le nécessite.
