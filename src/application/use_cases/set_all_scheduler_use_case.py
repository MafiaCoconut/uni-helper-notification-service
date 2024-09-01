from datetime import datetime, timedelta

from application.interfaces.scheduler_interface import SchedulerInterface
from application.services.notification_service import NotificationService
from application.services.users_service import UsersService
from application.use_cases.set_canteens_mailing_job_use_case import SetCanteensMailingJobUseCase
from application.use_cases.set_s3_scheduler_job import SetS3JobUseCase
from domain.entities.job import Job


# from application.services.scheduler_service import SchedulerService
# from application.repositories.meeting_repository import MeetingRepository
# from application.repositories.scheduler_repository import SchedulerRepository


class SetAllSchedulersJobsUseCase:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 users_service: UsersService,
                 set_canteens_mailing_job_use_case: SetCanteensMailingJobUseCase,
                 set_s3_jobs_use_case: SetS3JobUseCase,
                 ):

        self.scheduler_interface = scheduler_interface
        self.users_service = users_service
        self.set_canteens_mailing_job_use_case = set_canteens_mailing_job_use_case
        self.set_s3_jobs_use_case = set_s3_jobs_use_case

    async def execute(self):
        data = await self.users_service.get_users_all()

        for user in data:
            if user.mailing_time == '-' or user.status == "deactivated":
                continue
            else:
                await self.set_canteens_mailing_job_use_case.execute(
                    user_id=user.user_id, mailing_time=user.mailing_time
                )

        await self.set_s3_jobs_use_case.execute()

        await self.scheduler_interface.start()
