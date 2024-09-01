from application.interfaces.notification_gateway import NotificationGateway
from infrastructure.config.logs_config import log_decorator

import aiohttp

import os
import logging
from dotenv import load_dotenv
load_dotenv()

error_logger = logging.getLogger('error_logger')


class NotificationGatewayImpl(NotificationGateway):
    @staticmethod
    @log_decorator(print_args=False)
    async def send_canteens_menu(user_id: int) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f"{os.getenv('CORE_ADDRESS')}/notification/canteens_menu/{user_id}",
                    params={}
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")

    @staticmethod
    @log_decorator(print_args=False)
    async def send_admins_message(user_id: int, msg: str) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f"{os.getenv('CORE_ADDRESS')}/notification/admins_message/{user_id}",
                    params={}
            ) as resp:
                if resp.status == 200:
                    response_json = await resp.json()
                    return response_json
                else:
                    error_logger.error(f"Failed to get data. Response code: {resp.status}")



