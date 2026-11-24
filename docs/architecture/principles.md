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

## Séparations

17. Knowledge != Memory != State != Policy.
18. Authority != Permission != Approval ; Provenance != Authority.
19. Criticality != OperationalImpact.
20. Phase != Status != SupportStatus.
21. Result != Evidence != Memory.
22. Import != Merge != Sync.
23. Resource != Definition != Instance.
24. Geometry != Topology != Semantics.
25. Installed != Integrated != Validated != Supported ; UNKNOWN != SUPPORTED.
26. SchemaValid != ModelValid != RuntimeAuthorized.
27. Observation != Evaluation ; Evaluation != Policy.
28. Interface != Protocol != Capability.
29. Model-valid relationship != Observed relationship != Validated Knowledge.
30. Semantic consistency != Factual truth.
31. Dashboard != State != Evidence.
32. Log != Metric != Trace != Evidence ; ces signaux peuvent contribuer à produire ou étayer de l'EVIDENCE.
33. Available Library != Required Dependency.
34. Popular Technology != Architectural Requirement.

## Exécution et ALC

35. POLICY peut conduire notamment à ALLOW_AUTO, REQUIRE_APPROVAL, DRY_RUN_ONLY ou DENY.
36. ALC est un pattern d'orchestration, pas une primitive Core : `RESOLVE -> POLICY -> EXECUTE -> OBSERVE -> EVALUATE -> DISPOSE`.
37. Dispositions possibles : COMPLETE, CONTINUE, RETRY, REPLAN, ESCALATE, ABORT.
38. RETRY != REPLAN ; une nouvelle action à effet de bord issue d'un REPLAN repasse par POLICY.
39. Une boucle agentique est bornée explicitement ; elle ne modifie jamais automatiquement sa propre POLICY.
40. DRY_RUN != SHADOW_MODE ; Shadow Decision != Authorized Execution.

## Validation et connaissance

41. L1 Schema Validation vérifie structure, types, enums et invariants locaux.
42. L2 Model Validation vérifie Registry, références, relations, scopes d'Authority et cohérence du modèle.
43. L3 Runtime Validation vérifie State réel, PolicyDecision, Permission, Authority, Approval éventuelle, budgets, providers et autorisation effective.
44. Model Output != Evidence != Memory != Knowledge.
45. Pipeline d'apprentissage : événement réel -> RUN -> RESULT -> EVIDENCE -> Memory candidate -> qualification -> Memory -> validation/sourcing -> Knowledge candidate -> Knowledge.
46. Une relation autorisée par le modèle ne constitue pas une affirmation qu'elle existe dans le monde réel.
47. Une observation ne devient pas automatiquement Knowledge ; sa promotion exige qualification, sourcing et validation adaptés au contexte.
48. La gouvernance de Knowledge conserve le sens, la provenance, le contexte, le versioning pertinent et l'Authority applicable sans créer une primitive universelle supplémentaire.

## Observabilité

49. L'observabilité est une capacité transverse et une projection sur des responsabilités existantes, pas une nouvelle source de vérité.
50. Logs, métriques et traces conservent leur nature propre ; aucun n'est automatiquement EVIDENCE.
51. Les dashboards visualisent ou explorent des données ; ils ne deviennent ni State ni Evidence par leur seule présentation.
52. Un provider d'observabilité reste remplaçable et sa panne ne doit pas rendre indisponible la fonction primaire des systèmes métier.

## Intégrations et dépendances

53. MCP, API, CLI, OSC et mécanismes similaires restent des protocoles/interfaces ou implémentations d'intégration ; ils ne deviennent pas des primitives Core.
54. Une base vectorielle, un moteur RAG, un framework agentique, un serveur API ou un outil d'observabilité n'entre dans le runtime que si une CAPABILITY concrète le justifie.
55. CAPABILITY != Library ; SKILL != Library ; Provider != Library.
56. La popularité d'une technologie, sa présence dans un stack de référence ou sa disponibilité locale ne justifient ni son installation ni son intégration.

## Développement

57. Le repository Git est la référence versionnée du projet.
58. Progression privilégiée : prototype -> DRY_RUN -> SHADOW_MODE -> controlled execution -> EVIDENCE -> evaluation.
59. Petite modification -> validation -> test -> commit -> utilisation -> Evidence -> décision suivante.
60. Pour v0.0.1, la solution minimale testable et réversible prime sur la sophistication prématurée.
