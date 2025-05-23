from app.configuration import Config
from app.emulator import Scraper
from app.emulator.parser import Parser
from ..database import DisciplineDao, get_postgres

def scrap_and_parse():
    with get_postgres() as session:
        dao = DisciplineDao(session=session)
        with Scraper(Config.SAZ_INSTRUCTION) as sc:
            for i, url in enumerate(Config.SAZ_INSTRUCTION.URLS_TO_PARSE):
                sc.connect_main_page(url)
                parser = Parser(sc.page_source)
                all_disc = parser.parse().all_disciplines
                dao.insert_all(all_disc)



if __name__ == '__main__':
    with get_postgres() as session:
        dao = DisciplineDao(session=session)
        print(dao.get(code='320112'))
