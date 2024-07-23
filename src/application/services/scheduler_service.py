# src/application/services/scheduler_service.py
from datetime import datetime

from application.interfaces.scheduler_interface import SchedulerInterface
from application.use_cases.set_all_scheduler_use_case import SetAllSchedulersJobsUseCase


class SchedulerService:
    def __init__(self, scheduler: SchedulerInterface):
        self.scheduler = scheduler
        self.set_all_schedulers_jobs = SetAllSchedulersJobsUseCase()

    def add_job(self, job: Job) -> None:
        self.scheduler.add_job(job)

    def add_all_jobs(self, jobs: list) -> None:
        for job in jobs:
            self.scheduler.add_job(job)
                # func=job.func,
                # trigger=job.trigger,
                # run_date=job.run_date,
                # args=job.args
            # )

    def delete_job(self, job_id: str) -> None:
        self.scheduler.delete_job(job_id)
