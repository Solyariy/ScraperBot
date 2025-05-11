from typing import Annotated
from pydantic import StringConstraints

class Config:
    URL_PATTERN = Annotated[str, StringConstraints(pattern=r"https?://[-.a-zA-Z]{1,}")]
