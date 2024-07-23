from abc import ABC, abstractmethod


class NotificationWebInterface(ABC):
    @staticmethod
    @abstractmethod
    async def send_canteens_menu(user_id: int) -> None:
        pass

    @staticmethod
    @abstractmethod
    async def send_admins_message(self, user_id: int, msg: str) -> None:
        pass

