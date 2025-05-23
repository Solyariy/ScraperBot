from bs4 import BeautifulSoup
import pandas as pd
from .card_parser import CardParser


class Parser(BeautifulSoup):
    def __init__(self, html_text):
        super().__init__(html_text, features="lxml")
        self.all_disciplines = []
        self.dataframe = None

    def parse(self):
        if len(self.all_disciplines) != 0:
            return self
        cards = self.select("div[id='w1'] div[class='panel-group'] div[class='panel panel-default']")
        for card in cards:
            card_parser = CardParser(card)
            card_parser.get_general_info().get_semester_info().get_speciality_info()
            self.all_disciplines.extend(card_parser.disciplines)
        return self

    def to_dataframe(self):
        if self.dataframe: return self.dataframe
        dict_disciplines = [discipline.model_dump() for discipline in self.all_disciplines]
        self.dataframe = pd.DataFrame(data=dict_disciplines)
        return self.dataframe

    def to_csv(self, name):
        if not self.dataframe:
            self.to_dataframe()
        self.dataframe.to_csv(f"/Users/mac/Desktop/Python_DS/ScraperEmulator/files/{name}")


if __name__ == '__main__':
    with open("/Users/mac/Desktop/Python_DS/ScraperEmulator/html_2", "r") as f:
        html_data = f.read()
    parser = Parser(html_data)
    parser.parse().to_csv("test_df")
