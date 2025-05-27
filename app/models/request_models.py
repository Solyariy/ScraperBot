from datetime import datetime
from typing import Any, Optional

from fastapi import HTTPException
from pydantic import BaseModel


class ModelException(HTTPException):
    def __init__(self, model_class: type[BaseModel]):
        match name := model_class.__name__:
            case "DisciplineGet" | "DisciplineUpdateSet":
                message = f"At least 1 parameter needed to {name[-3:]} row"
            case "DisciplineUpdateFind":
                message = "Need an id or (code and specialty) to UPDATE row"
            case "DisciplineDelete":
                message = "Need an id or (code and specialty) to DELETE row"
            case "DisciplineInsert":
                message = ("Need code, name, specialty, kind, year, "
                           "faculty, cathedra, education_level "
                           "to INSERT row")
            case _:
                message = "UNKNOWN ERROR"
        super().__init__(status_code=422, detail=message)


class BaseDiscipline(BaseModel):
    id: Optional[int] = None
    code: Optional[int] = None
    name: Optional[str] = None
    specialty: Optional[str] = None
    kind: Optional[str] = None
    semester: Optional[str] = None
    year: Optional[int] = None
    credits_ects: Optional[str] = None
    hours: Optional[str] = None
    students_max: Optional[str] = None
    groups_max: Optional[str] = None
    one_group_range: Optional[str] = None
    faculty: Optional[str] = None
    cathedra: Optional[str] = None
    education_level: Optional[str] = None
    lecturer: Optional[str] = None
    is_deleted: Optional[bool] = None
    deletion_time: Optional[datetime] = None

    def no_none_dump(self):
        return self.model_dump(exclude_none=True)

    def __str__(self):
        return str(self.no_none_dump())


class DisciplineGet(BaseDiscipline):
    def __init__(self, **kwargs):
        if not kwargs:
            raise ModelException(self.__class__)
        super().__init__(**kwargs)


class DisciplineUpdateFind(BaseDiscipline):
    def __init__(self, **kwargs):
        if kwargs.get("id") or (kwargs.get("code") and kwargs.get("specialty")):
            super().__init__(**kwargs)
        else:
            raise ModelException(self.__class__)


class DisciplineUpdateSet(DisciplineGet):
    pass


class DisciplineUpdate(BaseModel):
    to_find: DisciplineUpdateFind
    to_update: DisciplineUpdateSet

    def __str__(self):
        return (f"DisciplineUpdate("
                f"to_find={self.to_find.no_none_dump()}; "
                f"to_update={self.to_update.no_none_dump()})")


class DisciplineDelete(DisciplineUpdateFind):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class DisciplineInsert(BaseDiscipline):
    def __init__(self, **kwargs):
        if not {"code", "name", "specialty", "kind", "year",
                "faculty", "cathedra", "education_level"}.issubset(kwargs.keys()):
            raise ModelException(self.__class__)
        super().__init__(**kwargs)


class DisciplineInsertContainer(BaseModel):
    container: list[DisciplineInsert]

    def __init__(self, **kwargs):
        container = [DisciplineInsert(**disc) for disc in kwargs.values()]
        super().__init__(container=container)
