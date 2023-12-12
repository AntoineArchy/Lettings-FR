# CI/CD et Déploiement

Ce document décrit le processus de CI/CD et les étapes de déploiement du projet.

## Pipeline CI/CD

Le pipeline CI/CD est conçu pour automatiser la construction, les tests, la conteneurisation, et le déploiement du
projet.

### Étapes du pipeline :

Lors d'un push sur le repo :

1. **Compilation et Tests :**
    - Reproduit l'environnement de développement local.
    - Exécute le linting, les tests unitaires, et vérifie que la couverture de test est supérieure à 80%.

Dans le cas ou le push concerne la branche principale ET que la suite de tests s'est exécutée sans erreurs, alors :

2. **Conteneurisation :**

- Construit une image Docker du site.
- Tague les images avec le "hash" de commit.
- Pousse l'image vers le registre des conteneurs Docker Hub.

[FUTURE]
Dans le cas ou le push concerne la branche principale ET que la conteneurisation s'est exécutée sans erreurs, alors :

3. **Déploiement en Production :**
    - Met en service le site sur Azure.

## Fonctionnement

L'automatisation repose sur des [Github Action](https://github.com/features/actions). Le détail du workflow est
consultables dans le fichier [pipeline.yml](../workflows/pipeline.yml)

## Prérequis

Un compte Docker avec accès au projet est requis.
Afin de s'exécuter correctement et de manière sécurisée, la pipeline CI/CD s'appuie sur
des [Github Secret](https://github.com/features/actions).
Les secrets nécessaires sont :

- DOCKER_USERNAME : Votre nom d'utilisateur Docker
- DOCKER_PASSWORD : Votre mot de passe Docker
  [FUTURE :]
- DOCKER_REPO : Le repository docker sur lequel vous souhaitez push
- Infos liée à Azure

## Conteneurisation

Le travail de conteneurisation repose sur [Docker](https://docs.docker.com/).

### Build

- `cd /path/to/Python-OC-Lettings-FR`
- `docker build -t lettings-fr .`

### Run

- `docker run -dp 127.0.0.1:3000:3000 lettings-fr`
- Rendez vous sur http://127.0.0.1:3000/