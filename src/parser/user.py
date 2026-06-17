import os
from logging import Logger

import yaml

from models.entity import Entity


def parse_users(logger: Logger, users: list[Entity], output_dir: str = "output"):
    os.makedirs(f"{output_dir}", exist_ok=True)

    try:
        with open(f"{output_dir}/users.yaml", "w") as file:
            yaml.dump(users, file)
            logger.info(f"Saved users to {output_dir}/users.yaml")

    except Exception:
        raise
