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

    async def start(self) -> None:
        self.scheduler.start()

    async def add_job(self, job: Job) -> None:
        self.scheduler.add_job(
            func=job.func,
            trigger=job.trigger,
            hour=job.hour,
            minute=job.minute,
            args=job.args,
            id=job.id,
            day_of_week=job.day_of_week,
        )

    async def delete_job(self, job_id: str):
        self.scheduler.remove_job(job_id=job_id)

    async def get_all_jobs(self) -> list[str]:
        jobs = self.scheduler.get_jobs()
        return [f"Job ID: {job.id}, Next Run Time: {job.next_run_time}" for job in jobs]





