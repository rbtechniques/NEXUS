
import logging
import os

os.makedirs("data", exist_ok=True)

logging.basicConfig(
    filename="data/nexus.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)


def log_activity(message):
    logging.info(message)
