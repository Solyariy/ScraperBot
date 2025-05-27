import re

from bs4 import Tag

from ..models import Discipline


class CardParser:
    def __init__(self, card: Tag):
        self.body = card.find("table", attrs={"class": "table table-condensed table-bordered"})
        self.info: dict[str, str | int | float | None] = {"name": card.find("h4").text.strip()}
        self.disciplines: list[Discipline] = []

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
        semester_info = self.body.find("tr", string=re.compile(r"Деталі по семестрах"))
        if not semester_info:
            return self
        semester_info = semester_info.previous
        self.info["semester"] = semester_info.find("th", string=re.compile(r"(Осінь|Весна|Літо)")).text.strip()
        self.info["credits_ects"], self.info["hours"], *_ = [item.text.split()[0] for item in
                                                             semester_info.select("tr:nth-child(3) > td > span")]
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
        return self

    def get_speciality_info(self):
        for spec_info in self.body.select("tbody > tr tr"):
            self.info["specialty"], self.info["kind"] = [item.text.strip() for item in spec_info.find_all("td")]
            self.disciplines.append(Discipline(**self.info))
