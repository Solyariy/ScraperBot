from typing import Optional

from fastapi import APIRouter, Depends

from ..configuration import logger
from ..database import DisciplineDao, get_postgres
from ..models import (DisciplineDelete, DisciplineGet,
                      DisciplineInsertContainer, DisciplineUpdate)

router = APIRouter(prefix="/api/v1")


@router.get("/root/{val}")
def main(val:bool, one: Optional[int] = None, two: Optional[str] = None, three: Optional[bool] = None):
    if val:
        return f"HELLO {one=}, {two=}, {three=}"
    return f"HELLO"


@router.get("/disc")
async def find(body: DisciplineGet, session=Depends(get_postgres)):
    dao = DisciplineDao(session)
    logger.debug(msg=str(body))
    return dao.get(body)


@router.post("/disc")
async def update(bodies: DisciplineUpdate, session=Depends(get_postgres)):
    dao = DisciplineDao(session)
    logger.debug(msg=str(bodies))
    return dao.update(bodies.to_find, bodies.to_update)

@router.put("/disc")
async def insert(body: DisciplineInsertContainer, session=Depends(get_postgres)):
    dao = DisciplineDao(session)
    logger.debug(msg=str(body))
    if len(body.container) == 1:
        return dao.insert(body.container[0])
    return dao.insert_all(body)


@router.delete("/disc")
async def delete(body: DisciplineDelete, session=Depends(get_postgres)):
    dao = DisciplineDao(session)
    logger.debug(msg=str(body))
    return dao.delete(body)

