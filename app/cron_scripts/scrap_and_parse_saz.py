from ..configuration import Config
from ..database import DisciplineDao, get_postgres
from ..emulator import Parser, Scraper


def scrap_and_parse(with_options: bool = False):
    with get_postgres() as session:
        dao = DisciplineDao(session=session)
        with Scraper(Config.SAZ_INSTRUCTION, with_options=with_options) as sc:
            for url in Config.SAZ_INSTRUCTION.URLS_TO_PARSE:
                sc.connect_main_page(url)
                parser = Parser(sc.page_source)
                all_disc = parser.parse().all_disciplines
                dao.insert_all(all_disc)


if __name__ == '__main__':
    scrap_and_parse(with_options=True)
