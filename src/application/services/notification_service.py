from application.interfaces.notification_gateway import NotificationGateway
from application.use_cases.send_admins_mailing_message_notification_use_case import \
    SendAdminsMailingMessageNotificationUseCase
from application.use_cases.send_canteens_menu_notification_use_case import SendCanteensMenuNotificationUseCase
from application.use_cases.update_users_mailing_time_use_case import UpdateUsersMailingTimeUseCase
from infrastructure.config.logs_config import log_decorator


class NotificationService:
    def __init__(self,
                 notification_interface: NotificationGateway,
                 ):
        self.notification_interface = notification_interface
        self.send_canteens_menu_use_case = SendCanteensMenuNotificationUseCase(
            notification_interface=notification_interface
        )
        self.send_admins_mailing_message_use_case = SendAdminsMailingMessageNotificationUseCase(
            notification_interface=notification_interface
        )


    @log_decorator(print_args=False)
    async def send_canteen_menu(self):
        await self.send_canteens_menu_use_case.execute()

    @log_decorator(print_args=False)
    async def send_admins_mailing_message(self, users: list[int]):
        await self.send_admins_mailing_message_use_case.execute(users=users)

