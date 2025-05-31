from fastapi import APIRouter, Depends

from ..database import DisciplineDaoAsync, get_async_postgres
from ..models import (DisciplineDelete, DisciplineGet,
                      DisciplineInsertContainer, DisciplineUpdate)

router = APIRouter(prefix="/api/v3")


@router.get("/root/{val}")
async def main(val: int):
    if val:
        return f"HELLO ASYNC {val=}"
    return f"HELLO ASYNC"


@router.get("/disc")
async def find(body: DisciplineGet, session=Depends(get_async_postgres)):
    dao = DisciplineDaoAsync(session)
    return await dao.get(body)


@router.post("/disc")
async def update(bodies: DisciplineUpdate, session=Depends(get_async_postgres)):
    dao = DisciplineDaoAsync(session)
    return await dao.update(bodies.to_find, bodies.to_update)

@router.put("/disc")
async def insert(body: DisciplineInsertContainer, session=Depends(get_async_postgres)):
    dao = DisciplineDaoAsync(session)
    if len(body.container) == 1:
        return await dao.insert(body.container[0])
    return await dao.insert_all(body)


@router.delete("/disc")
async def delete(body: DisciplineDelete, session=Depends(get_async_postgres)):
    dao = DisciplineDaoAsync(session)
    return await dao.delete(body)

