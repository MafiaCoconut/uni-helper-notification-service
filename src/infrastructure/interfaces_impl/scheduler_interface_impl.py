from typing import List

from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.notification_service import NotificationService
from application.services.users_service import UsersService
from domain.entities.job import Job
from apscheduler.schedulers.asyncio import AsyncIOScheduler


class SchedulerInterfaceImpl(SchedulerInterface):
    def __init__(self,
                 notification_service: NotificationService,
                 users_service: UsersService,
                 scheduler: AsyncIOScheduler
                 ):
        self.notification_service = notification_service
        self.users_service = users_service
        self.scheduler = scheduler

    async def add_job(self, job: Job) -> None:
        self.scheduler.add_job(
            func=job.func,
            trigger=job.trigger,
            hour=job.hour,
            minute=job.minute,
            args=job.args,
            id=job.job_id

        )

    async def set_all_jobs(self):
        data = await self.users_service.get_user_id_and_mailing_time()
        print(data)

        for user in data:
            print(user)
            if user.get('mailing_time') == '-':
                continue
            hour, minute = user.get('mailing_time').split(':')

            await self.add_job(Job(
                func=self.notification_service.send_canteen_menu,
                trigger='cron',
                hour=hour,
                minute=minute,
                args=[user.get('user_id')],
                job_id=f"canteens_menu {user.get('user_id')}"
            ))

        self.scheduler.start()



