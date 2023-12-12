# Interfaces de Programmation

Cette section fournit un aperçu des composants clés de l'application, y compris les vues, les URLs, et les templates.
Les modèles sont détaillés à la rubrique : [Structure de la Base de Données](StructureBaseDeDonnees.md)

## Vues

### index

- Chemin : ""
- Fonction : `index`
- Description : Vue pour la page d'accueil.

### lettings_index

- Chemin : "lettings/"
- Fonction : `lettings_index`
- Description : Vue pour afficher la liste des locations.

### letting

- Chemin : "lettings/<int:letting_id>/"
- Fonction : `letting`
- Description : Vue pour afficher les détails d'une location spécifique.

### profiles_index

- Chemin : "profiles/"
- Fonction : `profiles_index`
- Description : Vue pour afficher la liste des profils d'utilisateurs.

### profile

- Chemin : "profiles/<str:username>/"
- Fonction : `profile`
- Description : Vue pour afficher le profil d'un utilisateur spécifique.

## URLs

- "" : Page d'accueil (`index`).
- "lettings/" : Liste des locations (`lettings_index`).
- "lettings/<int:letting_id>/" : Détails d'une location spécifique (`letting`).
- "profiles/" : Liste des profils d'utilisateurs (`profiles_index`).
- "profiles/<str:username>/" : Profil d'un utilisateur spécifique (`profile`).
- "admin/" : Section d'administration Django.

## Templates

Les templates sont situés dans le répertoire "templates" à la racine du projet.

- `base.html`
- `index.html`
- `lettings_index.html`
- `letting.html`
- `profiles_index.html`
- `profile.html`