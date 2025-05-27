from .logger import setup_logging


def lifespan(app):
    setup_logging()
    yield
