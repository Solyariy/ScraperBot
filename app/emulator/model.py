from pydantic import BaseModel
from typing import Optional


class Discipline(BaseModel):
    id_: Optional[int]
    code: int
    name: str
    specialty: str
    kind: str
    semester: Optional[str]
    year: int
    credits_ects: Optional[str]
    hours: Optional[str]
    students_max: Optional[str]
    groups_max: Optional[str]
    one_group_range: Optional[str]
    faculty: str
    cathedra: str
    education_level: str
    lecturer: Optional[str]

    class Config:
        orm_mode = True
