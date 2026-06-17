import asyncio
import sys

import telethon
from telethon import TelegramClient
from telethon.tl.custom.dialog import Dialog

from config.env import Cfg, InvalidEnvException, get_user_env
from config.logger import init_logger
from models.entity import Entity
from parser.channel import parse_channels
from parser.group import parse_groups
from parser.user import parse_users


async def main():
    channels: list[Entity] = []
    groups: list[Entity] = []
    users: list[Entity] = []

    logger = init_logger("telegrid")

    try:
        cfg: Cfg = get_user_env()

        async with TelegramClient(
            "anon", cfg.TELEGRAM_API_ID, cfg.TELEGRAM_API_HASH
        ) as client:
            logger.info("Connection successful")

            dialogs: list[Dialog] = await client.get_dialogs(limit=None)

            for dialog in dialogs:
                if dialog.is_channel:
                    # Telethon and Telegram's internal APIs insert -100* at the beginning of channel ids
                    # and make group ids negative so its easier to recognize the peer type at glance.
                    # We therefore need to resolve the real id
                    # https://docs.telethon.dev/en/stable/concepts/chats-vs-channels.html#converting-ids
                    real_id, _ = telethon.utils.resolve_id(dialog.id)

                    channels.append(
                        Entity(
                            name=dialog.name,
                            id=real_id,
                        )
                    )
                elif dialog.is_group:
                    real_id, _ = telethon.utils.resolve_id(dialog.id)

                    groups.append(
                        Entity(
                            name=dialog.name,
                            id=real_id,
                        )
                    )
                elif dialog.is_user:
                    users.append(
                        Entity(
                            name=dialog.name,
                            id=dialog.id,
                        )
                    )

        parse_channels(logger, channels)
        parse_groups(logger, groups)
        parse_users(logger, users)

    except InvalidEnvException as e:
        logger.warning(e)
        sys.exit(1)

    except Exception as e:
        logger.critical(e)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
