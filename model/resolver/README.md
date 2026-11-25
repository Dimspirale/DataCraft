# Resolvers

RESOLVER propose ou sélectionne une stratégie, un provider, un backend ou une cible appropriée à partir d'une intention structurée, du contexte applicable, de RESOURCE et de STATE, sans modifier l'autorité de POLICY.

## Invariants

- `Current Plan != Original Intent`.
- `Replan != Intent Mutation`.
- `Derived Goal != User Intent != Authorized Goal`.
- `Planning != Retrieval`.
- `Reasoning Technique != Plan`.
- `Generated Plan != Authorized Plan`.
- `Model Selection != Execution Authorization`.
- `Provider Selection != Execution Authorization`.
- `Alternative Available != Failover Authorized`.

RESOLVER peut adapter la stratégie et proposer un REPLAN. Il ne peut pas modifier silencieusement l'intention structurée, POLICY, Authority, Permission, Approval ou ce qui est considéré comme vrai.

Toute nouvelle action à effet de bord issue d'un REPLAN, d'un failover, d'une récupération ou d'un rollback doit repasser par POLICY avant EXECUTION.

ALC reste un pattern d'orchestration borné :

`RESOLVE -> POLICY -> EXECUTE -> OBSERVE -> EVALUATE -> DISPOSE`

avec notamment `COMPLETE`, `CONTINUE`, `RETRY`, `REPLAN`, `ESCALATE` et `ABORT`. `RETRY != REPLAN`.

Les mécanismes appelés model routing, agent routing, provider selection, load balancing ou failover selection peuvent être des stratégies de résolution lorsque leur besoin est démontré ; ils ne créent pas pour autant de nouvelles primitives Core ni un Cognitive Core universel.
