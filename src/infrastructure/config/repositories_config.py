from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from infrastructure.db.base import get_db, async_engine
from infrastructure.repositories_impl.users_repository_impl import UsersRepositoryImpl


def get_users_repository() -> UsersRepositoryImpl:
    # return UsersRepositoryImpl(session=get_db())
    session = AsyncSession(bind=async_engine, expire_on_commit=False)
    return UsersRepositoryImpl(session=session)

