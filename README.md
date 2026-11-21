# DataCraft v0.0.1

DataCraft est un cockpit cognitif local-first et offline-ready. Ce dépôt démarre par le modèle canonique avant les implémentations.

## Chaîne architecturale
PROJECT -> PROFILE -> CAPABILITY -> SKILL -> POLICY -> RESOLVER -> CON/ADP/ENG -> SYS

## Principes
- Un métier est un PROFILE, pas un agent.
- Handle interne immuable; ID humain canonique; anciens IDs conservés comme aliases; Path mutable.
- ARCH décrit l'architecture; ADR enregistre une décision.
- P0 START / P1 GO / P2 BUILD / P3 NEXT sont séparées du statut et de la criticité.
- Les logiciels externes sont remplaçables et ne constituent jamais le Core.
- UNKNOWN != SUPPORTED.
- Import != Merge != Sync.
- Resource / Definition / Instance sont séparés.
- Knowledge / Memory / State / Policy sont séparés.
- Policy avant exécution; sandbox; observabilité; gateway LLM.

## P0 START
Le premier contrat de sécurité est `CAP.SECURITY.OS_CONFINEMENT`.
