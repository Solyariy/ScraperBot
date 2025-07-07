from contextlib import contextmanager

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker

from ..configuration import Config

engine = sa.create_engine(Config.POSTGRES_URL, echo=True, pool_pre_ping=True)

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
