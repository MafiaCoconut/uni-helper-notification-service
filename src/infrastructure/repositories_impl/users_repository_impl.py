from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.repositories.users_repository import UsersRepository
from infrastructure.db.models.user_orm import UserOrm


class UsersRepositoryImpl(UsersRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_id_and_mailing_time(self):
        query = select(UserOrm.user_id, UserOrm.mailing_time)
        result = await self.session.execute(query)
        rows = result.fetchall()
        return [{"user_id": row.user_id, "mailing_time": row.mailing_time} for row in rows]
