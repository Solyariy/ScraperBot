from bs4 import BeautifulSoup, PageElement, Tag, NavigableString
from model import Discipline


class CardParser:
    def __init__(self, card: PageElement | Tag | NavigableString):
        self.body = card.find("table", attrs={"class": "table table-condensed table-bordered"})
        self.info: dict[str, str | int | float | None] = {"name": card.find("h4").text.strip()}
        self.disciplines: list[Discipline] = []

    def get_cards(self):
        return self.body.select("div[id='w1'] div[class='panel-group'] div[class='panel panel-default']")

    def get_general_info(self):
        faculty_info = self.body.select_one("tbody:nth-child(1)")
        self.info["code"] = int(faculty_info.select_one("tr:nth-child(1) > td").text.strip())
        self.info["year"] = int(faculty_info.select_one("tr:nth-child(2) > td > span:nth-child(3)").text.strip()[0])
        self.info["faculty"] = faculty_info.select_one("tr:nth-child(3) > td").text.strip()
        self.info["cathedra"] = faculty_info.select_one("tr:nth-child(4) > td").text.strip()
        self.info["education_level"] = faculty_info.select_one("tr:nth-child(5) > td").text.strip()
        if faculty_info.select_one("tr:nth-child(7) > th"):
            self.info["lecturer"] = faculty_info.select_one("tr:nth-child(7) > td").text.strip()
        else:
            self.info["lecturer"] = None
        return self

    def get_semester_info(self):
        semester_info = self.body.select_one("tbody:nth-child(2) > tr:nth-child(3)")
        self.info["semester"] = semester_info.find("th").text.strip()
        self.info["credits_ects"], self.info["hours"], *_ = [float(item.text.split()[0]) for item in
                                                   semester_info.select("td > span")[:2]]
        groups_info = self.body.select_one("tbody:nth-child(3)")
        self.info["students_max"], self.info["groups_max"], self.info["one_group_range"], *_ = [
            item.text.strip() for item in groups_info.select("tr > td")
        ]
        self.info["one_group_range"] = (
            self.info["one_group_range"]
            .replace("\t", "")
            .replace("\n", "")
            .replace("від", "")
            .replace("до", "-")
        )
        self.info.update(info)
        return self

    def get_speciality_info(self):
        for spec_info in self.body.select("tbody > tr tr"):
            info["specialty"], info["kind"] = [item.text.strip() for item in spec_info.find_all("td")]
            self.disciplines.append(Discipline(**info))

if __name__ == '__main__':
    with open("/Users/mac/Desktop/Python_DS/ScraperEmulator/html_2", "r") as f:
        html_data = f.read()
    parser = Parser(html_data)
    cards = parser.select("div[id='w1'] div[class='panel-group'] div[class='panel panel-default']")
    cont = []
    for card in cards:

        # info: dict[str, str | int | float | None] = {"name": card.find("h4").text.strip()}
        # dd = {}
        # body = card.find("table", attrs={"class": "table table-condensed table-bordered"})
        #
        # faculty_info = body.select_one("tbody:nth-child(1)")
        # info["code"] = int(faculty_info.select_one("tr:nth-child(1) > td").text.strip())
        # info["year"] = int(faculty_info.select_one("tr:nth-child(2) > td > span:nth-child(3)").text.strip()[0])
        # info["faculty"] = faculty_info.select_one("tr:nth-child(3) > td").text.strip()
        # info["cathedra"] = faculty_info.select_one("tr:nth-child(4) > td").text.strip()
        # info["education_level"] = faculty_info.select_one("tr:nth-child(5) > td").text.strip()
        # if faculty_info.select_one("tr:nth-child(7) > th"):
        #     info["lecturer"] = faculty_info.select_one("tr:nth-child(7) > td").text.strip()
        # else:
        #     info["lecturer"] = None
        #
        # semester_info = body.select_one("tbody:nth-child(2) > tr:nth-child(3)")
        # info["semester"] = semester_info.find("th").text.strip()
        # info["credits_ects"], info["hours"], *_ = [float(item.text.split()[0]) for item in
        #                                            semester_info.select("td > span")[:2]]
        # groups_info = body.select_one("tbody:nth-child(3)")
        # info["students_max"], info["groups_max"], info["one_group_range"], *_ = [
        #     item.text.strip() for item in groups_info.select("tr > td")
        # ]
        # info["one_group_range"] = (
        #     info["one_group_range"]
        #     .replace("\t", "")
        #     .replace("\n", "")
        #     .replace("від", "")
        #     .replace("до", "-")
        # )
        # for spec_info in body.select("tbody > tr tr"):
        #     info["specialty"], info["kind"] = [item.text.strip() for item in spec_info.find_all("td")]
        #     cont.append(Discipline(**info))
    print(cont)

