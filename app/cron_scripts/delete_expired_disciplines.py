import asyncio
from datetime import datetime

from ..database import DisciplineDaoAsync, get_async_postgres_manager


async def delete_expired():
    now = datetime.now()
    async with get_async_postgres_manager() as session:
        dao = DisciplineDaoAsync(session=session)
        deleted = await dao.get_deleted()
        deleted_disc = [
            discipline
            for discipline in deleted
            if (now - discipline.deletion_time).days > 30
        ]
        res = await dao.hard_delete(deleted_disc)
    return res


if __name__ == '__main__':
    asyncio.run(delete_expired())
