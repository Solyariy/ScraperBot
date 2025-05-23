from pydantic import BaseModel
from typing import Optional
from numpy import isnan


class Discipline(BaseModel):
    code: int
    name: str
    specialty: str
    kind: str
    semester: Optional[str]
    year: int
    credits_ects: Optional[str]
    hours: Optional[float]
    students_max: Optional[str]
    groups_max: Optional[str]
    one_group_range: Optional[str]
    faculty: str
    cathedra: str
    education_level: str
    lecturer: Optional[str]

    # def __init__(self, data):
    #     for key, val in data.items():
    #         if isinstance(val, float) and isnan(val):
    #             data[key] = None
    #     super().__init__(**data)

    model_config = {
        "from_attributes": True
    }
