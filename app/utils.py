from logging import getLogger

logger = getLogger("main_logger")


def log(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            logger.debug(msg=f"SUCCESS at {func.__name__}()")
            return res
        except Exception as e:
            logger.error(msg=f"'{str(e).upper()}' at {func.__name__}()")
            raise
    return wrapper