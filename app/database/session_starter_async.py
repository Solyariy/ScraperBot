from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from ..configuration import Config

engine_async = create_async_engine(
    f"postgresql+asyncpg://"
    f"{Config.POSTGRES_USERNAME}:{Config.POSTGRES_PASSWORD}@localhost:5433"
    f"/SazScraper", echo=True)

AsyncSession = async_sessionmaker(bind=engine_async)


@asynccontextmanager
async def get_async_postgres_manager():
    async with AsyncSession() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise


async def get_async_postgres():
    async with AsyncSession() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
