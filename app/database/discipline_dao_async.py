import asyncio
from datetime import datetime
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, insert

from ..models import (DisciplineDelete, DisciplineGet, DisciplineInsert,
                      DisciplineInsertContainer, DisciplineTable,
                      DisciplineUpdateFind, DisciplineUpdateSet)

from ..utils import log


class DisciplineDaoAsync:
    def __init__(self, session: AsyncSession):
        self.session = session

    @log
    async def insert(self, disc: DisciplineInsert):
        disc_orm = DisciplineTable(disc)
        self.session.add(disc_orm)

    @log
    async def insert_all(self, disc_list: DisciplineInsertContainer):
        disc_orm = [
            DisciplineTable(disc)
            for disc in disc_list.container
        ]
        query = insert(DisciplineTable).values(**disc_orm)
        res = await self.session.execute(query)
        return res.scalars().fetchall()


    async def get_deleted(self):
        return await self.__get({'is_deleted': True})

    async def get(self, disc: DisciplineGet):
        query_dict = disc.no_none_dump()
        query_dict['is_deleted'] = False
        return await self.__get(query_dict)

    @log
    async def __get(self, query_dict):
        query = select(DisciplineTable).filter_by(**query_dict)
        res = await self.session.execute(query)
        return res.scalars().fetchall()

    async def update(self, to_find: DisciplineUpdateFind, to_update: DisciplineUpdateSet):
        return await self.__update(to_find=to_find, to_update=to_update.no_none_dump())

    async def delete(self, params: DisciplineDelete):
        # do not delete but place a flag that it is 'deleted'
        return await self.__update(
            to_find=params,
            to_update={'is_deleted': True, 'deletion_time': datetime.now()}
        )

    @log
    async def __update(self, to_find: DisciplineUpdateFind, to_update: dict[str, Any]):
        query = update(DisciplineTable).filter_by(**to_find.no_none_dump()).values(**to_update)
        res = await self.session.execute(query)
        return res

    @log
    async def hard_delete(self, objs_to_delete):
        tasks = [
            asyncio.create_task(self.session.delete(obj))
            for obj in objs_to_delete
        ]
        await asyncio.gather(*tasks)
        return len(objs_to_delete)
