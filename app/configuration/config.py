import os
from typing import Annotated
from pydantic import StringConstraints
from .instructions import Dou, DistEdu, Saz
from selenium.webdriver.chrome.options import Options


class Config:
    URL_PATTERN = Annotated[str, StringConstraints(pattern=r"https?://[-.a-zA-Z]{1,}")]
    SAZ_INSTRUCTION = Saz
    DIST_EDU_INSTRUCTION = DistEdu
    DOU_INSTRUCTION = Dou
    (CHROME_OPTIONS := Options()).add_argument("--headless=new")
    POSTGRES_USERNAME = os.environ["POSTGRES_USERNAME"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
