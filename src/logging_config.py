import logging
from logging.handlers import RotatingFileHandler
import os
LOG_DIR = "../logs"
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logging():
    log_format = "%(asctime)s.%(msecs)06d [%(levelname)s] %(name)s: %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(
            level=logging.DEBUG,
            format=log_format,
            datefmt=date_format,
            handlers=[
                logging.StreamHandler(),
                RotatingFileHandler(
                    os.path.join(LOG_DIR, "app.log"),
                    maxBytes=500_000,
                    backupCount=5,
                    encoding="utf-8"
                )
            ]
        )
