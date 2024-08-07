from application.interfaces.notification_gateway import NotificationGateway


class SendAdminsMailingMessageNotificationUseCase:
    def __init__(self, notification_interface: NotificationGateway):
        self.notification_interface = notification_interface

    def execute(self, users: list[int]):
        pass