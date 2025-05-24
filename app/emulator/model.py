from datetime import datetime
from typing import Optional

from pydantic import BaseModel


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
    is_deleted: Optional[bool]
    deletion_time: Optional[datetime]

    # def __init__(self, data):
    #     for key, val in data.items():
    #         if isinstance(val, float) and isnan(val):
    #             data[key] = None
    #     super().__init__(**data)

    model_config = {
        "from_attributes": True
    }
