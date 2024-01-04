# Procédures de Test et Gestion des Erreurs

## Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

## Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

### Notes :

Le contrôle de la couverture des tests est automatiquement déclenché lors l'exécution des tests. Si la couverture des
tests est inférieurs au paramétrage présent dans setup.cfg ([tool:pytest]/addopts--cov-fail-under=80), une exception est
alors levée.

## Formatage

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `black . --check`

## Monitoring

Le monitoring de l'application Orange County Lettings est géré à l'aide du module logging, en
complément, une intégration avec Sentry a été mise en place pour capturer et analyser les erreurs.

### Configuration Sentry

Pour utiliser Sentry, veuillez définir le DNS de votre projet Sentry dans le fichier d'environnement (.env).
Assurez-vous que la variable SENTRY_DSN contient le lien DNS approprié pour votre projet.  
Ex :
`"SENTRY_DNS" = "https://examplePublicKey@o0.ingest.sentry.io/0"`

Additionnellement, afin de pouvoir permettre une execution pérénne du pipeline de test et déploiement automatique, il
est recommandé de renseigner votre SENTRY_DNS dans les secrets github.

Lors de la mise en place du déploiement du site, il faudra alors également renseigner un dns sentry dans les variables
d'environnements. Voir [déploiement](CI_CD_Deploiement.md#déploiement).