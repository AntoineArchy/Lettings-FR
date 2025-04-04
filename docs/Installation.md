# Installation

Cette section décrit les prérequis et les étapes d'installation et de démarrage rapide du projet.

# macOS / Linux

## Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

## Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
  `which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

## Définir les variables d'environnements

Pour certains de ses paramètres, l'application repose sur
des [variables d'environnements](https://docs.python.org/fr/3/library/os.html?highlight=env#os.getenv).
Un fichier .env avec des informations par défault est présent à la racine du projet, vous pouvez modifier ce fichier
afin d'y renseigner vos propres paramètres.

- Voir [Configuration Sentry](ProcedureTestEtGestionErreurs.md#monitoring)
- Voir [Configuration Docker](CI_CD_Deploiement.md#conteneurisation)
- Voir [Configuration Render](CI_CD_Deploiement.md#déploiement)

## Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

## Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

# Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`