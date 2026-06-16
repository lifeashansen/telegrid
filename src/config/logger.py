import logging
from logging import Logger


def init_logger(name: str) -> Logger:
    logger: Logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s      %(levelname)s     %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger
