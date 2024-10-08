from application.interfaces.notification_gateway import NotificationGateway


class SendCanteensMenuNotificationUseCase:
    def __init__(self, notification_interface: NotificationGateway):
        self.notification_interface = notification_interface

    async def execute(self):
        await self.notification_interface.send_canteens_menu()

