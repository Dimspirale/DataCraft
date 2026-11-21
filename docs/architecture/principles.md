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

## Exécution et ALC

28. POLICY peut conduire notamment à ALLOW_AUTO, REQUIRE_APPROVAL, DRY_RUN_ONLY ou DENY.
29. ALC est un pattern d'orchestration, pas une primitive Core : `RESOLVE -> POLICY -> EXECUTE -> OBSERVE -> EVALUATE -> DISPOSE`.
30. Dispositions possibles : COMPLETE, CONTINUE, RETRY, REPLAN, ESCALATE, ABORT.
31. RETRY != REPLAN ; une nouvelle action à effet de bord issue d'un REPLAN repasse par POLICY.
32. Une boucle agentique est bornée explicitement ; elle ne modifie jamais automatiquement sa propre POLICY.
33. DRY_RUN != SHADOW_MODE ; Shadow Decision != Authorized Execution.

## Validation et connaissance

34. L1 Schema Validation vérifie structure, types, enums et invariants locaux.
35. L2 Model Validation vérifie Registry, références, relations, scopes d'Authority et cohérence du modèle.
36. L3 Runtime Validation vérifie State réel, PolicyDecision, Permission, Authority, Approval éventuelle, budgets, providers et autorisation effective.
37. Model Output != Evidence != Memory != Knowledge.
38. Pipeline d'apprentissage : événement réel -> RUN -> RESULT -> EVIDENCE -> Memory candidate -> qualification -> Memory -> validation/sourcing -> Knowledge candidate -> Knowledge.

## Développement

39. Le repository Git est la référence versionnée du projet.
40. Progression privilégiée : prototype -> DRY_RUN -> SHADOW_MODE -> controlled execution -> EVIDENCE -> evaluation.
41. Petite modification -> validation -> test -> commit -> utilisation -> Evidence -> décision suivante.
42. Pour v0.0.1, la solution minimale testable et réversible prime sur la sophistication prématurée.
