from fastapi import FastAPI

from .configuration import lifespan
from .routers import discipline_router

app = FastAPI(lifespan=lifespan)

app.include_router(discipline_router)

