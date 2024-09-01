from application.gateways.users_gateway import UsersGateway
from domain.entities.user import User


class UsersService:
    def __init__(self, users_gateway: UsersGateway):
        self.users_gateway = users_gateway

    async def get_user(self, user_id) -> User:
        return await self.users_gateway.get_user(user_id=user_id)

    async def get_users_all(self) -> list[User]:
        return await self.users_gateway.get_users_all()



