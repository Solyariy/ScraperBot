from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Discipline(BaseModel):
    code: Optional[int]
    name: Optional[str]
    specialty: Optional[str]
    kind: Optional[str]
    semester: Optional[str]
    year: Optional[int]
    credits_ects: Optional[str]
    hours: Optional[str]
    students_max: Optional[str]
    groups_max: Optional[str]
    one_group_range: Optional[str]
    faculty: Optional[str]
    cathedra: Optional[str]
    education_level: Optional[str]
    lecturer: Optional[str]
    is_deleted: Optional[bool]
    deletion_time: Optional[datetime]

    model_config = {
        "from_attributes": True
    }

