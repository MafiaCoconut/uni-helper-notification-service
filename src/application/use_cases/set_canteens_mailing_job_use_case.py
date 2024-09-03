from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.notification_service import NotificationService
from domain.entities.job import Job


class SetCanteensMailingJobUseCase:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 notification_service: NotificationService
                 ):
        self.scheduler_interface = scheduler_interface
        self.notification_service = notification_service

    async def execute(self, mailing_time: str):
        hour, minute = mailing_time.split(':')

        await self.scheduler_interface.add_job(
            Job(
                func=self.notification_service.send_canteen_menu,
                trigger='cron',
                hour=hour,
                minute=minute,
                day_of_week='mon-fri',
                id=f"canteens_menu {mailing_time}",
            ))

