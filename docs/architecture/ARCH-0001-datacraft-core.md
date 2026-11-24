# ARCH-0001 - DataCraft Core v0.0.1

## Objet
Définir le squelette model-centric du Core DataCraft.

## Chaîne canonique
`PROJECT -> PROFILE -> CAPABILITY -> SKILL -> POLICY -> RESOLVER -> EXECUTION -> RUN -> RESULT -> EVIDENCE`

Cette chaîne exprime des responsabilités. Elle ne doit pas être remplacée par une arborescence de fichiers, une hiérarchie d'agents, une liste de fournisseurs, un protocole d'intégration ou un stack technologique.

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
- Interface != Protocol != Capability.
- Model-valid relationship != Observed relationship != Validated Knowledge.
- Semantic consistency != Factual truth.
- Dashboard != State != Evidence.
- Log != Metric != Trace != Evidence.
- Available Library != Required Dependency.
- Popular Technology != Architectural Requirement.

## Knowledge et relations
Le modèle peut définir le sens des objets, les relations permises et les invariants sans affirmer que ces relations existent réellement. Une relation observée doit conserver sa provenance et son contexte. Une observation n'est pas automatiquement une connaissance validée.

Knowledge reste distinct de Memory, State et Evidence. La gouvernance de Knowledge porte notamment la provenance, le contexte, le versioning pertinent et les scopes d'Authority applicables sans introduire un Knowledge Harness universel comme nouvelle primitive Core.

## Observabilité
L'observabilité exploite des responsabilités existantes. Logs, métriques et traces peuvent contribuer à l'EVIDENCE, mais aucun de ces signaux n'est automatiquement EVIDENCE. Un dashboard est une projection de données et ne devient ni State, ni source de vérité, ni Authority.

Les outils d'observabilité restent des providers/intégrations remplaçables. Leur indisponibilité ne doit pas provoquer la panne de la fonction primaire des systèmes métier.

## Frontières d'intégration
- Les moteurs, frameworks, modèles et logiciels externes restent remplaçables et ne deviennent pas des primitives du Core uniquement parce qu'ils sont utilisés.
- Provider != Capability ; ENG != Core ; Development Tool != Runtime.
- MCP, API, CLI, OSC et mécanismes similaires restent des protocoles/interfaces ou des implémentations d'intégration.
- Une base vectorielle, un moteur RAG, un framework agentique ou un serveur API n'est introduit que lorsqu'une CAPABILITY concrète le requiert.
- CAPABILITY != Library ; SKILL != Library ; Provider != Library.
- Une source de vérité unique est définie par responsabilité.
- Les systèmes métier restent autonomes vis-à-vis de DataCraft : une panne de DataCraft ne doit pas provoquer la panne de leur fonction primaire.
