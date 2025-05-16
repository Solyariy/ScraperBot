from typing import Annotated
from pydantic import StringConstraints
from .instructions import Dou, DistEdu, Saz

class Config:
    URL_PATTERN = Annotated[str, StringConstraints(pattern=r"https?://[-.a-zA-Z]{1,}")]
    SAZ_INSTRUCTION = Saz
    DIST_EDU_INSTRUCTION = DistEdu
    DOU_INSTRUCTION = Dou

