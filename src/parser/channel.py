from logging import Logger

import yaml

from models.entity import Entity


def parse_channels(logger: Logger, channels: list[Entity], output_dir: str = "output"):
    try:
        with open(f"{output_dir}/channels.yaml", "w") as file:
            yaml.dump(channels, file)
            logger.info(f"Saved channels to {output_dir}/channels.yaml")

    except Exception:
        raise
