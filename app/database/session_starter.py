import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from app.configuration import Config

engine = sa.create_engine(
        f"postgresql+psycopg2://"
        f"{Config.POSTGRES_USERNAME}:{Config.POSTGRES_PASSWORD}@localhost"
        f"/SazScraper")

Session = sessionmaker(bind=engine)

def get_postgres():
    with Session() as session:
        yield session

def sth():
    i = 1
    yield i
    i += 1
    yield i

from app.database.table_model import DisciplineTable
from app.emulator.model import Discipline
import pandas as pd
if __name__ == '__main__':
    df = pd.read_csv("/Users/mac/Desktop/Python_DS/ScraperEmulator/files/df_0")
    # dt = DisciplineTable(*df.iloc[0])
    dd: pd.Series = df.iloc[2]
    print(Discipline(**dd.to_dict()))
    # sess = next(get_postgres())


