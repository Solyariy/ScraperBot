import os

from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()


class DouInstruction:
    LOGIN = [
        ((By.ID, "login-link"), "click"),
        ((By.ID, "_loginByMail"), "click"),
        ((By.CLASS_NAME, "txtEmail"), "send_mail"),
        ((By.CLASS_NAME, "txtPassword"), "send_password"),
        ((By.CLASS_NAME, "btnSubmit"), "click")
    ]
    MAIN_PAGE = "https://dou.ua"
    PASSWORD = os.environ.get("DOU_PASSWORD")
    MAIL = os.environ.get("DOU_MAIL")

