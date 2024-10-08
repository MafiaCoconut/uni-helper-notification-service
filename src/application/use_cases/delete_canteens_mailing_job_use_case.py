from application.exceptions.jobs_exceptions import JobNotExisted
from application.interfaces.scheduler_interface import SchedulerInterface
from infrastructure.config.logs_config import error_logger, system_logger


class DeleteCanteensMailingJobUseCase:
    def __init__(self,
                 scheduler_interface: SchedulerInterface,
                 ):
        self.scheduler_interface = scheduler_interface

    async def execute(self, user_id: int):
        try:
            await self.scheduler_interface.delete_job(f"canteens_menu {user_id}")
        except Exception as e:
            error_logger.error(e)
            system_logger.error(e)

            raise JobNotExisted()

