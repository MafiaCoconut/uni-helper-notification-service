# src/application/services/scheduler_service.py
from datetime import datetime

from application.interfaces.scheduler_interface import SchedulerInterface
from application.use_cases.set_all_scheduler_use_case import SetAllSchedulersJobsUseCase
from domain.entities.job import Job


class SchedulerService:
    def __init__(self, scheduler_interface: SchedulerInterface):
        self.scheduler_interface = scheduler_interface
        self.set_all_schedulers_jobs = SetAllSchedulersJobsUseCase(scheduler_interface=self.scheduler_interface)

    def add_job(self, job: Job) -> None:
        self.scheduler_interface.add_job(job)

    def add_all_jobs(self, jobs: list) -> None:
        for job in jobs:
            self.scheduler_interface.add_job(job)

    def delete_job(self, job_id: str) -> None:
        self.scheduler_interface.delete_job(job_id)

    async def config(self):
        await self.set_all_schedulers_jobs.execute()
