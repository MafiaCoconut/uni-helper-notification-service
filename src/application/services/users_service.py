from application.repositories.users_repository import UsersRepository


class UsersService:
    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    async def get_user_id_and_mailing_time(self) -> list[dict]:
        result = await self.user_repository.get_user_id_and_mailing_time()
        return result

