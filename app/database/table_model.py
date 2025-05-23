from datetime import datetime
from sqlalchemy import DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from ..emulator import Discipline
from .session_starter import Base


class DisciplineTable(Base):
    __tablename__ = "disciplines"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int]
    name: Mapped[str]
    specialty: Mapped[str]
    kind: Mapped[str]
    semester: Mapped[str | None]
    year: Mapped[int]
    credits_ects: Mapped[str | None]
    hours: Mapped[str | None]
    students_max: Mapped[str | None]
    groups_max: Mapped[str | None]
    one_group_range: Mapped[str | None]
    faculty: Mapped[str]
    cathedra: Mapped[str]
    education_level: Mapped[str]
    lecturer: Mapped[str | None]
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    deletion_time: Mapped[datetime | None] = mapped_column(DateTime, default=None)

    def __init__(self, clone_obj: Discipline):
        super().__init__(**clone_obj.model_dump())

    def __str__(self):
        return str(self.__dict__)
