from apscheduler.schedulers.asyncio import AsyncIOScheduler

from pytz import timezone

from application.services.scheduler_service import SchedulerService
from infrastructure.config.services_config import notification_service, users_service
from infrastructure.interfaces_impl.scheduler_interface_impl import SchedulerInterfaceImpl

scheduler = AsyncIOScheduler(timezone=timezone("Europe/Berlin"))


def get_scheduler_interface() -> SchedulerInterfaceImpl:
    return SchedulerInterfaceImpl(
        notification_service=notification_service,
        users_service=users_service,
        scheduler=scheduler
    )


def get_scheduler_service() -> SchedulerService:
    return SchedulerService(
        scheduler_interface=get_scheduler_interface(),
        notification_service=notification_service
    )
