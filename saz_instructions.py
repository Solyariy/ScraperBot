from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
load_dotenv()


class SazInstructions:
    LOGIN = [
        ((By.CSS_SELECTOR, "a[href='/auth/o365']"), "click"),
        ((By.XPATH, '//*[@id="i0116"]'), "send_mail+"),
        ((By.XPATH, '//*[@id="i0118"]'), "send_password+"),

    ]
    MAIN_PAGE = "https://my.ukma.edu.ua/"
    PASSWORD = os.environ.get("MICROSOFT_PASSWORD")
    MAIL = os.environ.get("MICROSOFT_MAIL")