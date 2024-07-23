# src/application/services/scheduler_service.py
from datetime import datetime

from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.notification_service import NotificationService
from application.use_cases.set_all_scheduler_use_case import SetAllSchedulersJobsUseCase
from application.use_cases.update_users_mailing_time_use_case import UpdateUsersMailingTimeUseCase
from domain.entities.job import Job


class SchedulerService:
    def __init__(self, scheduler_interface: SchedulerInterface, notification_service: NotificationService):
        self.scheduler_interface = scheduler_interface
        self.notification_service = notification_service
        self.set_all_schedulers_jobs = SetAllSchedulersJobsUseCase(scheduler_interface=self.scheduler_interface)
        self.update_mailing_time_use_case = UpdateUsersMailingTimeUseCase(scheduler_interface=self.scheduler_interface)

    async def add_job(self, job: Job) -> None:
        await self.scheduler_interface.add_job(job)

    def add_all_jobs(self, jobs: list) -> None:
        for job in jobs:
            self.scheduler_interface.add_job(job)

    async def delete_job(self, job_id: str) -> None:
        await self.scheduler_interface.delete_job(job_id)

    async def config(self):
        await self.set_all_schedulers_jobs.execute()

    async def update_mailing_time(self, user_id: int, new_mailing_time: str):
        await self.update_mailing_time_use_case.execute(user_id=user_id, new_mailing_time=new_mailing_time,
                                                        func=self.notification_service.send_canteen_menu)

    async def get_all_jobs(self):
        return await self.scheduler_interface.get_all_jobs()

