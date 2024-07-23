from application.interfaces.scheduler_interface import SchedulerInterface
from domain.entities.job import Job
from typing import Optional, Callable


class UpdateUsersMailingTimeUseCase:
    def __init__(self, scheduler_interface: SchedulerInterface):
        self.scheduler_interface = scheduler_interface

    async def execute(self, user_id: int, new_mailing_time: str, func: Callable):
        try:
            await self.scheduler_interface.delete_job(f'canteens_menu {user_id}')
        except:
            pass

        hour, minute = new_mailing_time.split(':')
        await self.scheduler_interface.add_job(
            Job(
                func=func,
                trigger='cron',
                hour=hour,
                minute=minute,
                args=[user_id],
                job_id=f'canteens_menu {user_id}',
            )
        )




