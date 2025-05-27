from contextlib import contextmanager

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker

from ..configuration import Config

engine = sa.create_engine(
    f"postgresql+psycopg2://"
    f"{Config.POSTGRES_USERNAME}:{Config.POSTGRES_PASSWORD}@localhost:5433"
    f"/SazScraper", echo=True)

Session = sessionmaker(bind=engine)
Base = declarative_base()


@contextmanager
def get_postgres_manager():
    with Session() as session:
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise


def get_postgres():
    with Session() as session:
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
