# Principes DataCraft v0.0.1

## Système

1. Local-first, offline-ready, cockpit-grade et hot-swappable.
2. Model-centric : l'arborescence de fichiers n'est pas l'ontologie.
3. Source de vérité unique par responsabilité.
4. Les systèmes métier restent autonomes vis-à-vis de DataCraft.
5. Les fournisseurs, frameworks, modèles et produits externes restent remplaçables.

## Responsabilités

6. Chaîne canonique : `PROJECT -> PROFILE -> CAPABILITY -> SKILL -> POLICY -> RESOLVER -> EXECUTION -> RUN -> RESULT -> EVIDENCE`.
7. Un métier est un PROFILE, pas un Agent.
8. CAPABILITY != Provider ; Provider != Execution Backend ; ENG != Core ; Development Tool != Runtime.
9. POLICY précède toute EXECUTION ayant un effet de bord.
10. RESOLVER propose ou sélectionne ; POLICY autorise ou interdit ; EXECUTION exécute ; RUN matérialise l'occurrence ; RESULT porte la sortie ; EVIDENCE porte la preuve exploitable.

## Identité

11. Handle = identité interne immuable.
12. ID = identifiant humain canonique.
13. Alias = ancien ID uniquement pour une correspondance 1:1.
14. Path = localisation mutable, jamais identité.
15. ExternalIdentity = identité dans un système externe.
16. Une transformation 1:n utilise une MIG explicite et auditable, pas des Alias artificiels.
17. Artifact Handle != Storage Path != External Object ID.

## Séparations

18. Knowledge != Memory != State != Policy.
19. Authority != Permission != Approval ; Provenance != Authority.
20. Criticality != OperationalImpact.
21. Phase != Status != SupportStatus.
22. Result != Evidence != Memory.
23. Import != Merge != Sync.
24. Resource != Definition != Instance.
25. Geometry != Topology != Semantics.
26. Installed != Integrated != Validated != Supported ; UNKNOWN != SUPPORTED.
27. SchemaValid != ModelValid != RuntimeAuthorized.
28. Observation != Evaluation ; Evaluation != Policy.
29. Interface != Protocol != Capability.
30. Model-valid relationship != Observed relationship != Validated Knowledge.
31. Semantic consistency != Factual truth.
32. Dashboard != State != Evidence.
33. Log != Metric != Trace != Evidence ; ces signaux peuvent contribuer à produire ou étayer de l'EVIDENCE.
34. Available Library != Required Dependency.
35. Popular Technology != Architectural Requirement.

## Stockage, artefacts et résilience

36. Metadata Path != Data Path != Control Path.
37. Unified Namespace != Unified Storage ; Unified Access != Unified Authority.
38. Artifact Located != Artifact Reachable ; Artifact Reachable != Artifact Valid.
39. Control Plane Available != Data Plane Available.
40. Snapshot != Backup != Replication != Immutability.
41. Protected != Restorable ; Restore Possible != Restore Tested.
42. Retention Policy != Proven Retention ; Backup Completed != Recovery Validated.
43. Capacity != Throughput != Latency != Availability.
44. Available Space != Suitable Storage ; Storage Reachable != Workload Ready.
45. Provider Healthy != End-to-End Capability Healthy.
46. Une opération de protection ou de restauration produit un RESULT ; sa vérification exploitable est une EVIDENCE distincte.
47. Le RESOLVER sélectionne un stockage ou provider selon RESOURCE, STATE et contexte ; l'emplacement ne devient pas l'identité de l'artefact.

## Exécution et ALC

48. POLICY peut conduire notamment à ALLOW_AUTO, REQUIRE_APPROVAL, DRY_RUN_ONLY ou DENY.
49. ALC est un pattern d'orchestration, pas une primitive Core : `RESOLVE -> POLICY -> EXECUTE -> OBSERVE -> EVALUATE -> DISPOSE`.
50. Dispositions possibles : COMPLETE, CONTINUE, RETRY, REPLAN, ESCALATE, ABORT.
51. RETRY != REPLAN ; une nouvelle action à effet de bord issue d'un REPLAN repasse par POLICY.
52. Une boucle agentique est bornée explicitement ; elle ne modifie jamais automatiquement sa propre POLICY.
53. DRY_RUN != SHADOW_MODE ; Shadow Decision != Authorized Execution.
54. API Capability Available != Operation Authorized.
55. Anomaly Detected != Remediation Authorized ; Recommended Action != Approved Action.
56. Automatable Repair != Safe Repair ; Self-Healing != Self-Authorizing.

## Validation et connaissance

57. L1 Schema Validation vérifie structure, types, enums et invariants locaux.
58. L2 Model Validation vérifie Registry, références, relations, scopes d'Authority et cohérence du modèle.
59. L3 Runtime Validation vérifie State réel, PolicyDecision, Permission, Authority, Approval éventuelle, budgets, providers et autorisation effective.
60. Model Output != Evidence != Memory != Knowledge.
61. Pipeline d'apprentissage : événement réel -> RUN -> RESULT -> EVIDENCE -> Memory candidate -> qualification -> Memory -> validation/sourcing -> Knowledge candidate -> Knowledge.
62. Une relation autorisée par le modèle ne constitue pas une affirmation qu'elle existe dans le monde réel.
63. Une observation ne devient pas automatiquement Knowledge ; sa promotion exige qualification, sourcing et validation adaptés au contexte.
64. La gouvernance de Knowledge conserve le sens, la provenance, le contexte, le versioning pertinent et l'Authority applicable sans créer une primitive universelle supplémentaire.

## Observabilité

65. L'observabilité est une capacité transverse et une projection sur des responsabilités existantes, pas une nouvelle source de vérité.
66. Logs, métriques et traces conservent leur nature propre ; aucun n'est automatiquement EVIDENCE.
67. Les dashboards visualisent ou explorent des données ; ils ne deviennent ni State ni Evidence par leur seule présentation.
68. Un provider d'observabilité reste remplaçable et sa panne ne doit pas rendre indisponible la fonction primaire des systèmes métier.

## Intégrations et dépendances

69. MCP, API, CLI, OSC et mécanismes similaires restent des protocoles/interfaces ou implémentations d'intégration ; ils ne deviennent pas des primitives Core.
70. Une base vectorielle, un moteur RAG, un framework agentique, un serveur API ou un outil d'observabilité n'entre dans le runtime que si une CAPABILITY concrète le justifie.
71. CAPABILITY != Library ; SKILL != Library ; Provider != Library.
72. La popularité d'une technologie, sa présence dans un stack de référence ou sa disponibilité locale ne justifient ni son installation ni son intégration.
73. Une architecture ou un produit de stockage spécialisé reste un provider ou une intégration potentielle ; ses objets propriétaires ne deviennent pas des primitives Core.
74. Kubernetes, Trident, pNFS, GPUDirect, cyber-vaults spécialisés, stockage distribué et intégration ONTAP/NetApp restent différés tant qu'une CAPABILITY concrète et de l'EVIDENCE ne les justifient pas.

## Développement

75. Le repository Git est la référence versionnée du projet.
76. Progression privilégiée : prototype -> DRY_RUN -> SHADOW_MODE -> controlled execution -> EVIDENCE -> evaluation.
77. Petite modification -> validation -> test -> commit -> utilisation -> Evidence -> décision suivante.
78. Pour v0.0.1, la solution minimale testable et réversible prime sur la sophistication prématurée.
79. Le premier scénario de stockage à privilégier est minimal : identité stable d'un artefact, plusieurs localisations possibles, observation d'accessibilité et d'intégrité, résolution de destination, POLICY avant copie, vérification post-exécution et production de RUN/RESULT/EVIDENCE.
