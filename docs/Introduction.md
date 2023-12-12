# Documentation Technique

Bienvenue dans la documentation technique de Orange County Lettings. Cette documentation vise à fournir une
compréhension approfondie des différents aspects du projet, allant de l'architecture du code aux processus de
déploiement.

## Aperçu du Projet

Le projet est une application web basée sur le framework Django. Il consiste en la refonte d'une architecture
monolithique actuelle en plusieurs applications distinctes. Cette optimisation implique la séparation des
fonctionnalités actuelles en deux nouvelles applications, "lettings" et "profiles". Les principales fonctionnalités du
projet comprennent :

- Gestion des locations : La partie "lettings" gère les informations liées aux locations, avec des modèles tels que "
  Address" et "Letting".
- Profils Utilisateurs : La partie "profiles" est dédiée à la gestion des profils utilisateurs, avec le modèle "
  Profile".

## Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell
exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

## Objectifs de la Documentation

Cette documentation a pour objectif de guider les développeurs, les contributeurs, et toute personne impliquée dans le
projet. Elle couvre les aspects suivants :

- [Installation du projet et démarrage rapide](Installation.md).
- [Technologies utilisées](Technologies.md).
- [Architecture de la base de données et modèles de données](StructureBaseDeDonnees.md).
- [Interfaces de programmation (vues, URLs, et templates)](InterfacesDeProgrammation.md).
- [Procédures de test et de gestion des erreurs](ProcedureTestEtGestionErreurs.md).
- [CI/CD et processus de déploiement](CI_CD_Deploiement.md).

## Comment Utiliser Cette Documentation

Chaque section de ce document est conçue pour couvrir un aspect spécifique du projet. Suivez les liens pour accéder
directement à la documentation pertinente.

