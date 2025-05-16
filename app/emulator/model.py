import re
from typing import Optional

from pydantic import BaseModel, Field
from enum import Enum


class Discipline(BaseModel):
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

