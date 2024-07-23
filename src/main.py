from fastapi import FastAPI

from contextlib import asynccontextmanager

from infrastructure.config import logs_config


@asynccontextmanager
async def lifespan(app):
    logs_config.config()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router)