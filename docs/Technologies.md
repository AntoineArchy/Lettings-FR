# Technologies

## Technologies Principales

- **Framework Django:** [Django](https://www.djangoproject.com/).
    - [Exécuter le site](Installation.md#exécuter-le-site)
    - [Administration](Installation.md#panel-dadministration)
- **Base de Données:** [SQLite](https://www.sqlite.org/index.html).
    - [Utilisation](StructureBaseDeDonnees.md#intéraction-avec-la-base-de-données)

## Outils de Développement

- **Testing:**  [Pytest](https://docs.pytest.org/en/7.4.x/changelog.html) /
  [Pytest-Django](https://pytest-django.readthedocs.io/en/latest/changelog.html).
    - [Utilisation](ProcedureTestEtGestionErreurs.md#tests-unitaires)
- **Linting:** [Flake8](https://flake8.pycqa.org/en/latest/release-notes/index.html).
    - [Utilisation](ProcedureTestEtGestionErreurs.md#linting)
- **Formatage:** [Black](https://black.readthedocs.io/en/stable/change_log.html).
    - [Utilisation](ProcedureTestEtGestionErreurs.md#formatage)
- **Monitoring**: [Sentry](https://sentry.io/welcome/)
    - [Utilisation](ProcedureTestEtGestionErreurs.md#monitoring)
- **Documentation
  **: [ReadTheDocs /w MkDocs](https://docs.readthedocs.io/en/stable/intro/getting-started-with-mkdocs.html)
    - Utilisation()
- **Hébergement**: [Render](https://render.com/)
    - Utilisation()
- **Convention d'écriture:** [Guide de développement](pdf/Guide%20de%20développement.pdf).

## Outils de Gestion de Projet

- **[GitHub](https://github.com/AntoineArchy/Lettings-FR/milestone/1?closed=1):** Contrôle de version, suivi des
  modifications, suivi des
  tickets.

## Outils CI/CD

- **[Docker](https://hub.docker.com/repository/docker/antoinetsz/letting-fr/general):** Utilisé pour la conteneurisation
  de l'application.
- **[GitHub Actions:](https://github.com/features/actions)** Mise en place d'un pipeline CI/CD pour automatiser les
  tests, le build et le déploiement.
    - [Détail de l'implémentation](CI_CD_Deploiement.md)
- **[Render](https://render.com/):** Hébergement et mise en place des variables d'environnements
  de l'application.
    - [Détail de l'utilisation](CI_CD_Deploiement.md)