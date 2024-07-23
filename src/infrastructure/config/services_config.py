
from application.services.notification_service import NotificationService
from application.services.users_service import UsersService
from infrastructure.config.interfaces_config import notification_interface
from infrastructure.config.repositories_config import get_users_repository


notification_service = NotificationService(
    notification_interface=notification_interface
)

users_service = UsersService(
    user_repository=get_users_repository()
)


# def get_users_service() -> UsersService:
#     return UsersService(user_repository=get_users_repository())
