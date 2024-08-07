from fastapi import FastAPI

from contextlib import asynccontextmanager

from infrastructure.config import logs_config
from infrastructure.config.scheduler_config import get_scheduler_service
from infrastructure.web.api import router


@asynccontextmanager
async def lifespan(app):
    logs_config.config()
    await get_scheduler_service().config()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router)
