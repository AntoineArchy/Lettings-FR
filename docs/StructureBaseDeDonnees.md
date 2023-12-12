# Structure de la Base de Données

Le projet utilise Django ORM pour définir et interagir avec la base de données. Ci-dessous, vous trouverez les modèles
de données principaux utilisés dans l'application.

## Modèles de Données

### Address

Le modèle `Address` représente une adresse physique avec les champs suivants :

- `number` : Numéro de rue (entier positif)
- `street` : Nom de la rue (chaîne de caractères)
- `city` : Ville (chaîne de caractères)
- `state` : État (chaîne de deux caractères)
- `zip_code` : Code postal (entier positif)
- `country_iso_code` : Code ISO du pays (chaîne de trois caractères)

### Letting

Le modèle `Letting` représente une location avec les champs suivants :

- `title` : Nom de la location (chaîne de caractères)
- `address` : Relation vers le modèle `Address` en utilisant une relation OneToOne.

### Profile

Le modèle `Profile` est lié au modèle utilisateur de Django (`User`) et représente le profil de l'utilisateur avec les
champs suivants :

- `user` : Relation vers le modèle utilisateur Django (`User`) en utilisant une relation OneToOne.
- `favorite_city` : Ville préférée de l'utilisateur (chaîne de caractères, facultatif).

## Diagramme de Base de Données

Voir : [Diagramme de la base de données](pdf/diagramme%20de%20la%20base%20de%20données.pdf) 