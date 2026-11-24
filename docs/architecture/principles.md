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
57. Multi-step AI Behavior != Agent Primitive.

## Validation, données et connaissance

58. L1 Schema Validation vérifie structure, types, enums et invariants locaux.
59. L2 Model Validation vérifie Registry, références, relations, scopes d'Authority et cohérence du modèle.
60. L3 Runtime Validation vérifie State réel, PolicyDecision, Permission, Authority, Approval éventuelle, budgets, providers et autorisation effective.
61. Model Output != Evidence != Memory != Knowledge.
62. Pipeline d'apprentissage : événement réel -> RUN -> RESULT -> EVIDENCE -> Memory candidate -> qualification -> Memory -> validation/sourcing -> Knowledge candidate -> Knowledge.
63. Dataset != Knowledge ; Recorded Observation != Ground Truth ; Feature != Fact.
64. Training Success != Generalization ; Model Fit != Operational Fitness.
65. Current Environment Fit != Architectural Generality ; les cas d'usage connus ne constituent pas automatiquement l'espace complet des exigences.
66. Correlation != Causation ; Prediction != Observation ; Classification != Authority ; Cluster Membership != Semantic Identity.
67. Normalization != Correction ; Correction != Source Mutation ; Missing != False ; Unknown != Invalid.
68. Une relation autorisée par le modèle ne constitue pas une affirmation qu'elle existe dans le monde réel.
69. Une observation ne devient pas automatiquement Knowledge ; sa promotion exige qualification, sourcing et validation adaptés au contexte.
70. La gouvernance de Knowledge conserve le sens, la provenance, le contexte, le versioning pertinent et l'Authority applicable sans créer une primitive universelle supplémentaire.
71. Lorsque des modèles apprenants sont évalués, les données ayant servi à l'apprentissage et celles utilisées pour évaluer la généralisation doivent rester distinguables. Le même principe de séparation des cas de construction et d'évaluation est privilégié pour les SKILL déterministes lorsque pertinent.

## Import et transformation

72. Un workflow d'import peut suivre `SOURCE -> EXTRACT -> NORMALIZE -> VALIDATE -> PROPOSE -> APPLY` sans créer une nouvelle chaîne de responsabilités Core.
73. Extraction != Transformation != Validation != Import ; Import != Merge != Sync.
74. PROPOSE ne confère aucune autorisation ; APPLY ayant un effet de bord repasse par POLICY.
75. Le nettoyage ou la normalisation ne modifie jamais silencieusement la source faisant autorité.

## Mobile, capture et contexte

76. Mobile Dim est une projection ou un rôle contextuel d'une RESOURCE, pas une primitive `MobileResource` ou `MobileAgent`.
77. Captured Data != Evidence != Knowledge ; Camera Observation != Validated Finding.
78. OS Permission != DataCraft Permission ; Permission Granted != Action Authorized.
79. Screen Visible != Authorized Context ; Accessible Data != Permitted Model Context.
80. Connected App != Trusted App.
81. La capture mobile privilégie `CAPTURE -> CLASSIFY -> ATTACH CONTEXT -> PROPOSE -> REVIEW`, puis qualification éventuelle en Evidence candidate, Memory candidate ou Action candidate.
82. Quick Capture, Focus Now, Next Action et Resume Context restent des patterns UX/CAPABILITY-SKILL ; aucune capture n'est promue automatiquement en Memory ou Knowledge.

## Observabilité

83. L'observabilité est une capacité transverse et une projection sur des responsabilités existantes, pas une nouvelle source de vérité.
84. Logs, métriques et traces conservent leur nature propre ; aucun n'est automatiquement EVIDENCE.
85. Les dashboards visualisent ou explorent des données ; ils ne deviennent ni State ni Evidence par leur seule présentation.
86. Un provider d'observabilité reste remplaçable et sa panne ne doit pas rendre indisponible la fonction primaire des systèmes métier.

## Git, CI et qualité

87. Pipeline Definition != Pipeline Run != Job Run != Artifact.
88. CI Job != SKILL ; Runner != EXECUTION ; Pipeline != RUN.
89. Merge Approval != Runtime Approval ; Review != Approval != Validation != Authorization.
90. CACHE != ARTIFACT != RESULT != EVIDENCE.
91. Scanner Output != Finding != Verdict ; Security Scan Passed != Runtime Authorized ; No Finding != Secure.
92. La CI est un mécanisme de développement et de validation pouvant exécuter L1/L2, tests et contrôles de sécurité et produire des artifacts ou éléments d'EVIDENCE ; elle n'est pas une nouvelle responsabilité Core.
93. Pour v0.0.1, privilégier diff/review, validations L1/L2, tests automatiques et secret scanning avant merge lorsque ces contrôles sont disponibles et proportionnés.
94. GitLab, GitHub Actions, runners et autres produits CI restent des Development Tools/providers remplaçables ; aucune dépendance GitLab n'est requise.

## Intégrations et dépendances

95. MCP, API, CLI, OSC et mécanismes similaires restent des protocoles/interfaces ou implémentations d'intégration ; ils ne deviennent pas des primitives Core.
96. Une base vectorielle, un moteur RAG, un framework agentique, un serveur API ou un outil d'observabilité n'entre dans le runtime que si une CAPABILITY concrète le justifie.
97. CAPABILITY != Library ; SKILL != Library ; Provider != Library.
98. La popularité d'une technologie, sa présence dans un stack de référence ou sa disponibilité locale ne justifient ni son installation ni son intégration.
99. Une architecture ou un produit de stockage spécialisé reste un provider ou une intégration potentielle ; ses objets propriétaires ne deviennent pas des primitives Core.
100. Kubernetes, Trident, pNFS, GPUDirect, cyber-vaults spécialisés, stockage distribué et intégration ONTAP/NetApp restent différés tant qu'une CAPABILITY concrète et de l'EVIDENCE ne les justifient pas.
101. Dataset, Feature, Pipeline, CIJob, Runner, Agent, MobileAgent et moteur ETL ne deviennent pas des primitives Core sans besoin architectural distinct démontré.

## Développement

102. Le repository Git est la référence versionnée du projet.
103. Progression privilégiée : prototype -> DRY_RUN -> SHADOW_MODE -> controlled execution -> EVIDENCE -> evaluation.
104. Petite modification -> validation -> test -> commit -> utilisation -> Evidence -> décision suivante.
105. Pour v0.0.1, la solution minimale testable et réversible prime sur la sophistication prématurée.
106. Le premier scénario de stockage à privilégier est minimal : identité stable d'un artefact, plusieurs localisations possibles, observation d'accessibilité et d'intégrité, résolution de destination, POLICY avant copie, vérification post-exécution et production de RUN/RESULT/EVIDENCE.
