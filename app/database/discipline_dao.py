from typing import Type, Any

from sqlalchemy import and_
from sqlalchemy.orm import Session

from ..emulator import Discipline
from .table_model import DisciplineTable
from .utils import get_common, check
from datetime import datetime

class DisciplineDao:
    def __init__(self, session: Session):
        self.session = session

    def insert(self, obj: Discipline):
        disc_orm = DisciplineTable(obj)
        self.session.add(disc_orm)

    def insert_all(self, obj_list: list[Discipline]):
        disc_orm = [
            DisciplineTable(obj)
            for obj in obj_list
        ]
        self.session.add_all(disc_orm)

    def get_expired(self):
        return self.__get({'is_deleted': True})

    def get(self, params: dict[str, Any]) -> list[Type[DisciplineTable]]:
        query_dict = get_common(params)
        query_dict['is_deleted'] = False
        return self.__get(query_dict)

    def __get(self, query_dict):
        res = self.session.query(DisciplineTable).filter_by(**query_dict).all()
        return res

    def update(self, to_find: dict[str, Any], to_update: dict[str, Any]):
        check(to_find)
        query_dict = get_common(to_update)
        res = self.session.query(DisciplineTable).filter_by(**to_find).update(query_dict)
        return res

    def delete(self, params: dict[str, Any]):
        # do not delete but place a flag that it is 'deleted'
        return self.update(
            to_find=params,
            to_update={'is_deleted': True, 'deletion_time': datetime.now()}
        )

    def hard_delete(self, params: dict[str, Any]):
        check(params)
        query_dict = get_common(params)
        res = self.session.query(DisciplineTable).filter_by(**query_dict).delete()
        return res

