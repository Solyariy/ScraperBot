from datetime import datetime
from typing import Any, Type

from sqlalchemy.orm import Session

from ..models import (DisciplineDelete, DisciplineGet, DisciplineInsert,
                      DisciplineInsertContainer, DisciplineTable,
                      DisciplineUpdateFind, DisciplineUpdateSet)


class DisciplineDao:
    def __init__(self, session: Session):
        self.session = session

    def insert(self, disc: DisciplineInsert):
        disc_orm = DisciplineTable(disc)
        self.session.add(disc_orm)

    def insert_all(self, disc_list: DisciplineInsertContainer):
        disc_orm = [
            DisciplineTable(disc)
            for disc in disc_list.container
        ]
        self.session.add_all(disc_orm)

    def get_deleted(self):
        return self.__get({'is_deleted': True})

    def get(self, disc: DisciplineGet) -> list[Type[DisciplineTable]]:
        query_dict = disc.no_none_dump()
        query_dict['is_deleted'] = False
        return self.__get(query_dict)

    def __get(self, query_dict):
        res = self.session.query(DisciplineTable).filter_by(**query_dict).all()
        return res

    def update(self, to_find: DisciplineUpdateFind, to_update: DisciplineUpdateSet):
        return self.__update(to_find=to_find, to_update=to_update.no_none_dump())

    def delete(self, params: DisciplineDelete):
        # do not delete but place a flag that it is 'deleted'
        return self.__update(
            to_find=params,
            to_update={'is_deleted': True, 'deletion_time': datetime.now()}
        )

    def __update(self, to_find: DisciplineUpdateFind, to_update: dict[str, Any]):
        res = (self.session.query(DisciplineTable)
               .filter_by(**to_find.no_none_dump())
               .update(to_update))
        return res

    def hard_delete(self, objs_to_delete):
        for obj in objs_to_delete:
            self.session.delete(obj)
        return len(objs_to_delete)
