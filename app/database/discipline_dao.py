from ..emulator import Discipline
from .table_model import DisciplineTable
from sqlalchemy.orm import Session


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
