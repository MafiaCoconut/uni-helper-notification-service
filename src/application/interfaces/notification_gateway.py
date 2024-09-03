from abc import ABC, abstractmethod


class NotificationGateway(ABC):
    @staticmethod
    @abstractmethod
    async def send_canteens_menu() -> None:
        pass

    @staticmethod
    @abstractmethod
    async def send_admins_message(self, user_id: int, msg: str) -> None:
        pass

