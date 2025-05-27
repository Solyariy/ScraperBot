import functools
import logging.config
import os
from logging import getLogger

import yaml

logger = getLogger("main_logger")


# TODO - call setup_logging at lifespan
def setup_logging():
    if not os.path.exists(path_ := os.path.join("app", "logs")):
        os.mkdir(path_)
    if not os.path.exists(file_ := os.path.join(path_, "main_logger.log")):
        with open(file_, "w"):
            pass
    config_path = os.path.join("app", "configuration", "logger_config.yaml")
    with open(config_path) as file:
        config = yaml.safe_load(file)
    logging.config.dictConfig(config)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            logger.info(msg=f"SUCCESS at {func.__name__}()")
            return res
        except Exception as e:
            logger.warning(msg=f"'{str(e).upper()}' at {func.__name__}()")
            raise
    return wrapper
