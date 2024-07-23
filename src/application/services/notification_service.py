from infrastructure.config.logs_config import log_decorator


class NotificationService:
    def __init__(self,
                 notification_interface: NotificationWebInterface,
                 ):
        self.notification_interface = notification_interface
        self.send_canteens_menu_use_case = SendCanteensMenuNotificationUseCase(
            notification_interface=notification_interface
        )
        self.send_admins_mailing_message_use_case = SendAdminsMailingMessageNotificationUseCase(
            notification_interface=notification_interface
        )

    @log_decorator
    def send_canteen_menu(self, user_id: int, locale: str):
        self.send_canteens_menu_notification_use_case.execute(user_id=user_id, locale=locale)

    @log_decorator
    def send_admins_mailing_message(self, users: list[int]):
        self.send_admins_mailing_message_notification_use_case.execute(users=users)
