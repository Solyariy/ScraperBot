from app.configuration import Config
from app.emulator import Scraper
from app.emulator.parser import Parser

from ..database import DisciplineDao, get_postgres


def scrap_and_parse(with_options: bool = False):
    with get_postgres() as session:
        dao = DisciplineDao(session=session)
        with Scraper(Config.SAZ_INSTRUCTION, with_options=with_options) as sc:
            for url in Config.SAZ_INSTRUCTION.URLS_TO_PARSE:
                sc.connect_main_page(url)
                parser = Parser(sc.page_source)
                all_disc = parser.parse().all_disciplines
                dao.insert_all(all_disc)

def hard_delete():
    now = datetime.now()
    with get_postgres() as session:
        dao = DisciplineDao(session=session)
        to_delete = dao.get_expired()
        dao.hard_delete(to_delete)

from datetime import datetime

if __name__ == '__main__':
    with get_postgres() as session:
        dao = DisciplineDao(session=session)
        res = dao.update(
            {'id': 12, 'code': 318403},
            {'is_deleted': False, 'deletion_time': None}
        )
        print(res)
    # print(type(datetime.now()))
