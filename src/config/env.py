import os

from exceptions import InvalidEnvException
from models.cfg import Cfg


def get_user_env() -> Cfg:
    TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
    TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")

    if TELEGRAM_API_ID is None:
        raise InvalidEnvException("$TELEGRAM_API_ID is required")

    if TELEGRAM_API_HASH is None:
        raise InvalidEnvException("$TELEGRAM_API_HASH is required")

    assert TELEGRAM_API_ID is not None
    assert TELEGRAM_API_HASH is not None

    return Cfg(int(TELEGRAM_API_ID), TELEGRAM_API_HASH)
