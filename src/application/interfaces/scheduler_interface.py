from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class SchedulerInterface(ABC):
    @abstractmethod
    async def start(self) -> None:
        pass

    @abstractmethod
    async def add_job(self, job) -> None:
        pass

    @abstractmethod
    async def delete_job(self, job_id: str) -> None:
        pass

    @abstractmethod
    async def get_all_jobs(self) -> list[str]:
        pass
