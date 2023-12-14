import datetime
import os
import sys
from dotenv import load_dotenv

import logging
from logging.handlers import TimedRotatingFileHandler

import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

load_dotenv()

log_directory = os.getenv("LOG_DIRECTORY", "logs")

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configuration du journal local
# Gestionnaire de fichiers rotatifs basé sur la date
log_filename = f"logs/{datetime.datetime.now().strftime('%Y-%m-%d')}.log"
daily_log_handler = TimedRotatingFileHandler(
    log_filename,
    when="midnight",
    interval=1,
    encoding="utf-8",
    delay=False,
)

log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
daily_log_handler.setFormatter(log_formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(daily_log_handler)

# Intégration à Sentry :
sentry_dsn = os.getenv("SENTRY_DSN", None)
print(sentry_dsn)
logging.error(sentry_dsn)
if sentry_dsn is not None:
    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[
            LoggingIntegration(
                level=logging.INFO,  # Capture info and above as breadcrumbs
                event_level=logging.WARNING,  # Send records as events
            ),
        ],
    )


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
