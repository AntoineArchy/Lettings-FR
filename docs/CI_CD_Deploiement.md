# CI/CD et Déploiement

Ce document décrit le processus de CI/CD et les étapes de déploiement du projet.

## Pipeline CI/CD

Le pipeline CI/CD est conçu pour automatiser la construction, les tests, la conteneurisation, et le déploiement du
projet.

### Étapes de la pipeline :

Lors d'un push sur le repo :

1. **Compilation et Tests :**
    - Reproduit l'environnement de développement local.
    - Exécute le linting, les tests unitaires, et vérifie que la couverture de test est supérieure à 80%.

Dans le cas ou le push concerne la branche principale ET que la suite de tests s'est exécutée sans erreurs, alors :

2. **Conteneurisation :**
    - Construit une image Docker du site.
    - Tague les images avec le "hash" de commit (et latest).
    - Pousse l'image vers le registre des conteneurs Docker Hub.

Dans le cas ou le push concerne la branche principale ET que la conteneurisation s'est exécutée sans erreurs, alors :

3. **Déploiement en Production :**
    - Met automatiquement la documentation [ReadTheDocs](https://readthedocs.org/) à jour

### Fonctionnement :

L'automatisation repose sur des [Github Action](https://github.com/features/actions). Le détail du workflow est
consultables dans les fichiers .github/workflows/

### Prérequis :

Un compte Docker avec accès au projet est requis pour la conteneurisation.
Un compte Render est requis pour le déploiement.
Afin de s'exécuter correctement et de manière sécurisée, la pipeline CI/CD s'appuie sur
des [Github Secret](https://github.com/features/actions).
Les secrets nécessaires sont :

- DOCKER_USERNAME : Votre nom d'utilisateur Docker
- DOCKER_PASSWORD : Votre mot de passe Docker
- DOCKER_REPO : Le repository docker sur lequel vous souhaitez push (Les identifiants "Username" et "Password" doivent
  être pourvu des droits nécessaires)
- RENDER_SERVICE_ID : Le [service_id](https://docs.render.com/environment-variables) render vous permettant le
  déploiement
- RENDER_API_KEY : Une de vos [clé d'API](https://docs.render.com/environment-variables) render
- SENTRY_DSN : Votre URL de projet Sentry, afin de reçevoir les messages d'erreurs et alertes sur votre tableau de bord
  sentry.

## Tests

L'exécution des Tests lors d'un push sur une des branches définie est entièrement automatique et ne requiert aucun
paramétrages autres que ceux présents dans le fichier ".github/workflows/quality_control.yml"
Assurez-vous d'avoir renseigné les secrets necessaries et détaillés dans la rubrique ci-dessus.

## Conteneurisation

Le travail de conteneurisation repose sur [Docker](https://docs.docker.com/). Une fois le container créé, celui-ci sera
alors push sur le repo parameter dans les secrets github (voir [CI/CD prérequis](CI_CD_Deploiement.md#prérequis)). Ce
conteneur sera taggé de deux façons : "latest", qui
identifie systématiquement le push le plus récent, ainsi que le SHA du commit github ayant déclenché la
containerisation.

#### Build manuel

- `cd /path/to/Python-OC-Lettings-FR`
- `docker build -t lettings-fr .`

#### Run

- `docker run -dp 127.0.0.1:3000:3000 lettings-fr`
- Rendez vous sur http://127.0.0.1:3000/

## Déploiement

Le site est actuellement hébergé sur [Render](https://render.com/).

### Paramétrage

Depuis la page de gestion du site render, à la rubrique "settings" section "Deploy" :

- Renseignez le champ "Image URL" avec les informations du repo Docker et le tag latest (Ex :
  docker.io/{DOCKER_USERNAME}/{DOCKER_REPO}:latest).

Depuis la page de gestion du site render, à la rubrique "Environment" section "Environment Variables" :

- Renseignez les champs "Key"/"Value" avec les clés / valeurs :
    - DJANGO_SECRET_KEY : Correspond à la constante "SECRET_KEY" présente dans le settings.py de l'application Django
    - LOG_DIRECTORY : Le repertoire dans lequel vous souhaitez voir les logs locaux en cas de défaillance sentry ("
      logs/" par défaut)
    - SENTRY_DSN : L'URL Sentry lié à votre projet, afin d'obtenir la consultation des logs en ligne.

Notes: Il est également possible de renseigner les variables d'environements sur render via un "Secret File", (voir
[Configuring Environment Variables and Secrets](https://docs.render.com/configure-environment-variables).)

Afin de permettre le bon déroulement du pipeline, assurez-vous d'avoir correctement renseigné les secrets github (
voir [CI/CD prérequis](CI_CD_Deploiement.md#prérequis)).

## Intégration ReadTheDocs

### Paramétrage

Les paramétrages nécessaires à l'intégration ReadTheDocs sont consultables dans les fichiers mkdocs.yml et
.readthedocs.yml. Afin de s'assuré de la compilation automatique de la doc, il est nécessaire de lié votre repo github (
Voir : [Importing your documentation](https://docs.readthedocs.io/en/stable/intro/import-guide.html)).