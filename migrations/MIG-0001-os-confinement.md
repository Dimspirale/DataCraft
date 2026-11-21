# MIG-0001 - OS_CONFINEMENT

## Source
Concept initial AppArmor comme couche de sécurité DataCraft.

## Mapping
- Concept générique de confinement OS: KEEP
- Dépendance AppArmor dans le Core: REMAP
- Cible canonique: TARGET `CAP.SECURITY.OS_CONFINEMENT`
- AppArmor: TARGET rôle ADP/ENG externe
- Formulation historique couplée au moteur: ARCHIVE

## Règle
Pas de retour en arrière vers un Core dépendant d'un moteur externe après migration canonique.
