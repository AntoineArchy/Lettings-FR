import datetime
import logging
import os
from logging.handlers import TimedRotatingFileHandler

import sentry_sdk
from dotenv import load_dotenv
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


def on_startup_log():
    logging.info("Project starting...")
