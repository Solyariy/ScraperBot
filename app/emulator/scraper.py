from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import time
from app.configuration import Config
from selenium.webdriver.common.keys import Keys
from pydantic import validate_call
from selenium.webdriver.chrome.options import Options

class Scraper(Chrome):
    def __init__(self, instructor, main_page_url=None):
        self.instructor = instructor
        self.main_page = main_page_url or instructor.MAIN_PAGE
        # options = Options()
        # options.add_argument("--headless=new")
        super().__init__(
            service=Service(
                executable_path="app/emulator/drivers/chromedriver"
            ),
            # options=options
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

from parser import Parser
if __name__ == '__main__':
    w = 137
    url_list = [
        (f"https://my.ukma.edu.ua/course"
         f"/catalog?filter%5Bacademic_year%5D%5B0%5D=2024"
         f"&filter%5Blevel%5D%5B0%5D=1&filter%5Blevel%5D%5B1%5D=2&filter%5Bselected%5D%5B0%5D=1"
         f"&page={i}") for i in range(1, w + 1)
    ]
    content = []
    with Scraper(Config.SAZ_INSTRUCTION) as em:
        for i, url in enumerate(url_list):
            em.connect_main_page(url)
            print(url)
            parser = Parser(em.page_source)
            parser.parse().to_csv(f"df_{i}")

