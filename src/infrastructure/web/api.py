from fastapi import Depends, APIRouter

from infrastructure.config.scheduler_config import scheduler_service
from infrastructure.config.services_config import notification_service

router = APIRouter()


@router.put('/update_mailing_time/{user_id}')
async def update_mailing_time(user_id: int, new_mailing_time: str):
    await scheduler_service.update_mailing_time(user_id=user_id, new_mailing_time=new_mailing_time)


@router.get('/jobs/all')
async def get_all_jobs():
    return {'text': await scheduler_service.get_all_jobs()}
