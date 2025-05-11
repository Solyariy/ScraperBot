from types import NoneType
import re
import bs4
from bs4 import BeautifulSoup
import aiohttp
from config import Config
from pydantic import BaseModel


async def get_page_content(
        full_url: Config.URL_PATTERN
):
    async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(full_url) as response:
            if response.status != 200:
                return
            html = await response.text(encoding="utf-8")
            return html


class Vacancy(BaseModel):
    date: str
    link: Config.URL_PATTERN
    salary: str | None

    def __init__(self, tag: bs4.element.Tag):
        date_ = tag.find("div", class_="date").text
        link_ = tag.find("a", class_="vt").get("href")
        try:
            salary_ = (tag.find("span", class_="salary")
                       .text
                       .replace(u"\xa0", " ")
                       .encode("utf-8"))
        except BaseException:
            salary_ = None
        super().__init__(date=date_, link=link_, salary=salary_)


if __name__ == '__main__':

    with open("html_test_3", "r") as file:
        soup = BeautifulSoup(file.read(), features="lxml")
        res = soup.select("div#vacancyListId ul")[0]
        print(res.prettify())
        kids = res.children
        for k in kids:
            print(k)
        vacancies = [
            Vacancy(tag=tag)
            for tag in res
        ]
        print(vacancies)

