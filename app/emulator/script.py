from app.configuration import Config
from app.emulator import Scraper
from app.emulator.parser import Parser


def scrap_and_parse():
    with Scraper(Config.SAZ_INSTRUCTION) as sc:
        for i, url in enumerate(Config.SAZ_INSTRUCTION.URLS_TO_PARSE):
            sc.connect_main_page(url)
            parser = Parser(sc.page_source)
            parser.parse().to_csv(f"df_{i}")

