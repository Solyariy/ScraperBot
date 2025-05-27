import time

from pydantic import validate_call
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from ..configuration import Config


class Scraper(Chrome):
    def __init__(self, instructor, main_page_url=None, with_options=False):
        self.instructor = instructor
        self.main_page = main_page_url or instructor.MAIN_PAGE
        super().__init__(
            service=Service(
                executable_path="app/emulator/drivers/chromedriver"
            ),
            options=Config.CHROME_OPTIONS if with_options else None
        )

    def login(self):
        for params, todo in self.instructor.LOGIN:
            res = self.find_element(*params)
            match todo:
                case "click":
                    res.click()
                case "send_mail":
                    res.send_keys(self.instructor.MAIL)
                case "send_mail+":
                    res.send_keys(self.instructor.MAIL, Keys.ENTER)
                case "send_password":
                    res.send_keys(self.instructor.PASSWORD)
                case "send_password+":
                    res.send_keys(self.instructor.PASSWORD, Keys.ENTER)
            time.sleep(1)

    @validate_call
    def connect_main_page(self, page_url: Config.URL_PATTERN | None = None):
        self.get(page_url or self.instructor.MAIN_PAGE)
        self.implicitly_wait(5)

    def __enter__(self):
        self.connect_main_page()
        self.login()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()
