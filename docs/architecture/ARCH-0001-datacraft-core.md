# ARCH-0001 - DataCraft Core v0.0.1

## Objet
Définir le squelette model-centric du Core DataCraft.

## Chaîne canonique
`PROJECT -> PROFILE -> CAPABILITY -> SKILL -> POLICY -> RESOLVER -> EXECUTION -> RUN -> RESULT -> EVIDENCE`

Cette chaîne exprime des responsabilités. Elle ne doit pas être remplacée par une arborescence de fichiers, une hiérarchie d'agents ou une liste de fournisseurs.

## Identité
- Handle : identité interne immuable.
- ID : identifiant humain canonique.
- Alias : ancien ID conservé uniquement pour une correspondance 1:1.
- Path : localisation mutable, jamais identité primaire.
- ExternalIdentity : identité d'un objet dans un système externe.
- Une transformation d'une ancienne entité en plusieurs nouvelles entités passe par une MIG explicite et auditable, pas par des Alias artificiels.

## Responsabilités d'exécution
- CAPABILITY décrit ce que DataCraft sait faire.
- SKILL porte une compétence ou procédure spécialisée mobilisable par une capacité.
- RESOLVER propose ou sélectionne une voie d'exécution.
- POLICY autorise, exige une approbation, limite au dry-run ou interdit l'action dans son contexte.
- EXECUTION exécute uniquement ce qui a été autorisé.
- RUN est l'occurrence concrète d'une exécution.
- RESULT est ce qui a été produit.
- EVIDENCE est ce qui peut servir de preuve de ce qui s'est produit.

## Séparations fondamentales
- Knowledge != Memory != State != Policy.
- Authority != Permission != Approval.
- Provenance != Authority.
- Criticality != OperationalImpact.
- Phase != Status != SupportStatus.
- Result != Evidence != Memory.
- SchemaValid != ModelValid != RuntimeAuthorized.

## Frontières
- Les moteurs, frameworks, modèles et logiciels externes restent remplaçables et ne deviennent pas des primitives du Core uniquement parce qu'ils sont utilisés.
- Provider != Capability ; ENG != Core ; Development Tool != Runtime.
- Une source de vérité unique est définie par responsabilité.
- Les systèmes métier restent autonomes vis-à-vis de DataCraft : une panne de DataCraft ne doit pas provoquer la panne de leur fonction primaire.
