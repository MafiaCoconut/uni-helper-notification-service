from infrastructure.interfaces_impl.notification_gateway_impl import NotificationGatewayImpl


def get_notification_interface() -> NotificationGatewayImpl:
    return NotificationGatewayImpl()




