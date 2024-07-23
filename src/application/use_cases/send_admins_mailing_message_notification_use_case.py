from application.interfaces.notification_web_interface import NotificationWebInterface


class SendAdminsMailingMessageNotificationUseCase:
    def __init__(self, notification_interface: NotificationWebInterface):
        self.notification_interface = notification_interface

    def execute(self, users: list[int]):
        pass