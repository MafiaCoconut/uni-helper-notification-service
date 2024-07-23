from application.interfaces.notification_web_interface import NotificationWebInterface


class SendCanteensMenuNotificationUseCase:
    def __init__(self, notification_interface: NotificationWebInterface):
        self.notification_interface = notification_interface

    def execute(self, user_id: int):
        self.notification_interface.send_canteens_menu(user_id=user_id)
