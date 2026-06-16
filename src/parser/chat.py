import sys
from logging import Logger

import yaml

from models.entity import Entity


def parse_chats(logger: Logger, chats: list[Entity], output_dir: str = "output"):
    try:
        with open(f"{output_dir}/chats.yaml", "w") as file:
            yaml.dump(chats, file)
            logger.info(f"Saved chats to {output_dir}/chats.yaml")

    except Exception as e:
        logger.critical(e)

        sys.exit(1)
