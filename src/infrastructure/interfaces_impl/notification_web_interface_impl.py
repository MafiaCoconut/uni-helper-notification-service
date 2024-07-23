from application.interfaces.notification_web_interface import NotificationWebInterface
from infrastructure.config.logs_config import log_decorator

import aiohttp

import os
import logging
from dotenv import load_dotenv
load_dotenv()

error_logger = logging.getLogger('error_logger')


class NotificationWebInterfaceImpl(NotificationWebInterface):
    @staticmethod
    @log_decorator
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
    @log_decorator
    async def send_admins_message(self, user_id: int, msg: str) -> None:
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




"""
async with aiohttp.ClientSession() as session:
    async with session.get(
            f"https://{os.getenv('CANTEEN_IP')}:{os.getenv('CANTEEN_MICRO_SVC_PORT')}/canteens_menu/{canteen_id}",
            params={'locale': locale}
    ) as resp:
        if resp.status == 200:
            response_json = await resp.json()
            return response_json
        else:
            error_logger.error(f"Failed to get data. Response code: {resp.status}")

"""