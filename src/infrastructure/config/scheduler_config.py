from apscheduler.schedulers.asyncio import AsyncIOScheduler

from pytz import timezone

from application.services.scheduler_service import SchedulerService
from infrastructure.config.services_config import notification_service, users_service
from infrastructure.interfaces_impl.scheduler_interface_impl import SchedulerInterfaceImpl

scheduler = AsyncIOScheduler(timezone=timezone("Europe/Berlin"))


scheduler_interface = SchedulerInterfaceImpl(
    notification_service=notification_service,
    users_service=users_service,
    scheduler=scheduler
)


schedulers_service = SchedulerService(
    scheduler_interface=scheduler_interface
)