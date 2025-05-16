from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import time
from app.configuration import Config
from selenium.webdriver.common.keys import Keys

class Emulator(Chrome):
    def __init__(self, instructor):
        self.instructor = instructor
        super().__init__(
            service=Service(
                executable_path="/Users/mac/Desktop/Python_DS/ScraperEmulator/chromedriver"
            )
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


    def connect_main_page(self):
        self.get(self.instructor.MAIN_PAGE)
        self.implicitly_wait(5)


if __name__ == '__main__':
    em = Emulator(Config.SazInstruction)
    em.connect_main_page()
    em.login()
    time.sleep(5)
    em.quit()
