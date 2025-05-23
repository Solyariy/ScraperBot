import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base
from app.configuration import Config
from contextlib import contextmanager

engine = sa.create_engine(
        f"postgresql+psycopg2://"
        f"{Config.POSTGRES_USERNAME}:{Config.POSTGRES_PASSWORD}@localhost:5433"
        f"/SazScraper")

Session = sessionmaker(bind=engine)
Base = declarative_base()

@contextmanager
def get_postgres():
    with Session() as session:
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
