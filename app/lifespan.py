from app.configuration.logger_setup import setup_logging
from app.database.session_starter_async import engine_async
from app.database.session_starter import engine
import asyncio


async def lifespan(app):
    setup_logging()
    yield
    await asyncio.to_thread(getattr(engine, "dispose"))
    await engine_async.dispose()
