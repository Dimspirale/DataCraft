# ADR-0001 - Abstraction OS_CONFINEMENT

- Status: ACCEPTED_FOR_V0.0.1
- Phase: P0_START

## Contexte
DataCraft exige un confinement OS sans coupler le Core à une technologie Linux particulière.

## Décision
Le Core expose `CAP.SECURITY.OS_CONFINEMENT`. La Policy DataCraft porte l'intention. Le Resolver sélectionne une réalisation. AppArmor, SELinux, Landlock, seccomp ou d'autres moteurs restent externes via ADP/ENG.

## Invariants
- Aucun moteur externe n'est le Core.
- UNKNOWN n'est jamais promu implicitement en SUPPORTED.
- AUDIT n'est pas équivalent à ENFORCE.
- Pour un scope critique en FAIL_CLOSED, l'exécution est interdite tant que l'enforcement requis n'est pas vérifié.
- L'état désiré et l'état observé restent distincts.
