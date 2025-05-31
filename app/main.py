from fastapi import FastAPI, Request, Response

from .lifespan import lifespan
from .routers import discipline_router, async_discipline_router
from time import perf_counter

app = FastAPI(lifespan=lifespan)

app.include_router(discipline_router)
app.include_router(async_discipline_router)


@app.middleware("http")
async def test_middleware(request: Request, call_next):
    start = perf_counter()
    response: Response = await call_next(request)
    spent_time = perf_counter() - start
    response.headers["X-Process-Time"] = str(spent_time)
    return response

