import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import ping
from app.db import init_db

log = logging.getLogger("uvicorn")


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info(" Starting up...")
    init_db(app)
    yield
    log.info("Shutting down...")


def create_application() -> FastAPI:
    application = FastAPI(lifespan=lifespan)
    application.include_router(ping.router)

    return application


app = create_application()
