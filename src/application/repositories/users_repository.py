from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class UsersRepository(ABC):
    @abstractmethod
    def __init__(self, session: AsyncSession):
        pass

    @abstractmethod
    async def get_user_id_and_mailing_time(self):
        pass


