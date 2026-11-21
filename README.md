# DataCraft v0.0.1

DataCraft est un cockpit cognitif model-centric, local-first et offline-ready pour assister le chef de projet et le directeur technique. Le dépôt Git constitue la référence versionnée du projet.

## Chaîne canonique de responsabilité

`PROJECT -> PROFILE -> CAPABILITY -> SKILL -> POLICY -> RESOLVER -> EXECUTION -> RUN -> RESULT -> EVIDENCE`

Cette chaîne décrit des responsabilités. L'arborescence de fichiers, les agents, providers, frameworks, modèles et produits externes ne constituent pas l'ontologie du Core.

## Principes structurants

- Un métier est un PROFILE, pas un Agent.
- CAPABILITY décrit ce que DataCraft sait faire ; un provider décrit éventuellement ce qui fournit cette capacité.
- Handle est l'identité interne immuable ; ID est l'identifiant humain canonique ; Alias conserve un ancien ID uniquement pour une correspondance 1:1 ; Path est mutable ; ExternalIdentity identifie un objet dans un système externe.
- ARCH décrit l'architecture et ses invariants ; ADR enregistre une décision ; MIG décrit une transformation historique auditable.
- Knowledge != Memory != State != Policy.
- Authority != Permission != Approval ; Provenance != Authority.
- Criticality != OperationalImpact.
- Phase != Status != SupportStatus.
- Result != Evidence != Memory.
- SchemaValid != ModelValid != RuntimeAuthorized.
- Import != Merge != Sync.
- Resource != Definition != Instance.
- Geometry != Topology != Semantics.
- Installed != Integrated != Validated != Supported ; UNKNOWN != SUPPORTED.
- Toute action à effet de bord passe par POLICY avant EXECUTION.
- Les systèmes métier restent autonomes : une panne de DataCraft ne doit pas provoquer la panne de leur fonction primaire.

## Exécution gouvernée

POLICY peut notamment produire `ALLOW_AUTO`, `REQUIRE_APPROVAL`, `DRY_RUN_ONLY` ou `DENY`.

Pour l'orchestration adaptative, DataCraft peut utiliser une boucle ALC bornée :

`RESOLVE -> POLICY -> EXECUTE -> OBSERVE -> EVALUATE -> DISPOSE`

avec `COMPLETE`, `CONTINUE`, `RETRY`, `REPLAN`, `ESCALATE` ou `ABORT` comme dispositions possibles. `RETRY != REPLAN` et toute nouvelle action à effet de bord issue d'un REPLAN repasse par POLICY.

## Développement v0.0.1

Le principe est :

`petite modification -> validation -> test -> commit -> utilisation -> Evidence -> décision suivante`

La sophistication n'est ajoutée que lorsqu'une CAPABILITY concrète et de l'EVIDENCE la justifient.

## P0 START

Le premier contrat de sécurité existant est `CAP.SECURITY.OS_CONFINEMENT`. Il reste en statut DRAFT et doit être validé aux niveaux SchemaValid, ModelValid et RuntimeAuthorized avant toute prétention d'autorisation runtime.
