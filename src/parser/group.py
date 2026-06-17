import os
from logging import Logger

import yaml

from models.entity import Entity


def parse_groups(logger: Logger, groups: list[Entity], output_dir: str = "output"):
    os.makedirs(f"{output_dir}", exist_ok=True)

    try:
        with open(f"{output_dir}/groups.yaml", "w") as file:
            yaml.dump(groups, file)
            logger.info(f"Saved groups to {output_dir}/groups.yaml")

    except Exception:
        raise
