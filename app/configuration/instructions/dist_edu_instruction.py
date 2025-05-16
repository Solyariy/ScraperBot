from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()


class DistEduInstruction:
    LOGIN = [
        ((By.XPATH, "//*[@id='region-main']/div/div/div/div/div/div/div[3]/div/a"), "click"),
        ((By.XPATH, '//*[@id="i0116"]'), "send_mail+"),
        ((By.XPATH, '//*[@id="i0118"]'), "send_password+"),

    ]
    MAIN_PAGE = "https://distedu.ukma.edu.ua/"
    PASSWORD = os.environ.get("MICROSOFT_PASSWORD")
    MAIL = os.environ.get("MICROSOFT_MAIL")
