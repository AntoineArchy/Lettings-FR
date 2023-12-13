# Procédures de Test et Gestion des Erreurs

## Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

## Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

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