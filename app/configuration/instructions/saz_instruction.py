from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
load_dotenv()


class SazInstruction:
    LOGIN = [
        ((By.CSS_SELECTOR, "a[href='/auth/o365']"), "click"),
        ((By.XPATH, '//*[@id="i0116"]'), "send_mail+"),
        ((By.XPATH, '//*[@id="i0118"]'), "send_password+"),
    ]
    MAIN_PAGE = "https://my.ukma.edu.ua/"
    URLS_TO_PARSE = [
        (f"https://my.ukma.edu.ua/course"
         f"/catalog?filter%5Bacademic_year%5D%5B0%5D=2024"
         f"&filter%5Blevel%5D%5B0%5D=1&filter%5Blevel%5D%5B1%5D=2&filter%5Bselected%5D%5B0%5D=1"
         f"&page={i}") for i in range(1, 138)
    ]
    PASSWORD = os.environ.get("MICROSOFT_PASSWORD")
    MAIL = os.environ.get("MICROSOFT_MAIL")

