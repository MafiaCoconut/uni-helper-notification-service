
from application.services.notification_service import NotificationService
from application.services.s3_service import S3Service
from application.services.users_service import UsersService
from infrastructure.config.interfaces_config import get_notification_interface
from infrastructure.config.repositories_config import get_users_repository
from infrastructure.config.s3_config import s3client

notification_service = NotificationService(
    notification_interface=get_notification_interface()
)

users_service = UsersService(
    user_repository=get_users_repository()
)

s3_service = S3Service(
    s3client=s3client
)


# def get_users_service() -> UsersService:
#     return UsersService(user_repository=get_users_repository())
