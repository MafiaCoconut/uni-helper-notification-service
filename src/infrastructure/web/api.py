from fastapi import Depends, APIRouter, Path, Response, status

from application.exceptions.jobs_exceptions import JobInvalidData
from application.services.scheduler_service import SchedulerService
from infrastructure.config.scheduler_config import get_scheduler_service
from infrastructure.config.services_config import notification_service

router = APIRouter()


@router.put('/user{user_id}/updateMailingTime')
async def update_mailing_time(
        user_id: int, new_mailing_time: str, response: Response,
        scheduler_service: SchedulerService = Depends(get_scheduler_service)
):
    try:
        await scheduler_service.update_mailing_time(user_id=user_id, new_mailing_time=new_mailing_time)
    except JobInvalidData as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'error': e}


@router.get('/jobs/getAll')
async def get_all_jobs(
        response: Response,
        scheduler_service: SchedulerService = Depends(get_scheduler_service)
):
    return {'text': await scheduler_service.get_all_jobs()}


@router.post('/user{user_id}/addUsersMailingTime')
async def create_new_users_job(
        user_id: int, mailing_time: str, response: Response,
        scheduler_service: SchedulerService = Depends(get_scheduler_service)
):
    try:
        await scheduler_service.update_mailing_time(user_id=user_id, new_mailing_time=mailing_time)
    except JobInvalidData as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'error': e}

