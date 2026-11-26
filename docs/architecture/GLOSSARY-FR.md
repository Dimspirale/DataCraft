# DataCraft — Glossaire pédagogique français

Les termes français servent à l'UX, aux visuels et à la pédagogie. Les identifiants anglais restent canoniques dans le modèle et le code.

| Français | Identifiant canonique | Sens pédagogique |
|---|---|---|
| Projet | `PROJECT` | Cadre métier dans lequel DataCraft travaille. |
| Profil | `PROFILE` | Point de vue métier mobilisé. |
| Capacité | `CAPABILITY` | Ce que DataCraft sait faire. |
| Savoir-faire | `SKILL` | Mise en œuvre spécialisée d'une capacité. |
| Politique | `POLICY` | Règles qui autorisent, contraignent ou interdisent une action. |
| Résolution | `RESOLVER` | Sélection/proposition de la meilleure manière de faire dans le contexte. |
| Action | `EXECUTION` | Action autorisée à réaliser. |
| Action réalisée | `RUN` | Instance réelle, datée et traçable d'une exécution. |
| Résultat | `RESULT` | Ce que le RUN produit. |
| Preuve | `EVIDENCE` | Éléments exploitables pour vérifier ce qui s'est réellement produit. |
| Ressource | `RESOURCE` | Objet ou mécanisme existant utilisable/observable. |
| État | `STATE` | Observation temporelle de la situation actuelle. |
| Connaissance | `KNOWLEDGE` | Savoir validé, sourcé et associé à une Authority appropriée. |
| Mémoire | `MEMORY` | Apprentissage qualifié issu de l'expérience, contextualisé et révisable. |

## ALC

ALC signifie **Agentic Loop Controlled**, traduit pédagogiquement par **Boucle Agentique Contrôlée**.

`RESOLVE -> POLICY -> EXECUTE -> OBSERVE -> EVALUATE -> DISPOSE`

Traduction pédagogique :

**RÉSOUDRE -> POLITIQUE -> EXÉCUTER -> OBSERVER -> ÉVALUER -> DÉCIDER**.

Dispositions :

- `COMPLETE` : TERMINER
- `CONTINUE` : CONTINUER
- `RETRY` : RÉESSAYER
- `REPLAN` : REPLANIFIER
- `ESCALATE` : ESCALADER
- `ABORT` : ABANDONNER / ARRÊTER

`RETRY != REPLAN`.

L'ALC est un pattern d'orchestration, pas une primitive métier et pas un Agent.
