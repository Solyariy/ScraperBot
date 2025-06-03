import os
import yaml
import logging.config


# call setup_logging at lifespan
def setup_logging():
    if not os.path.exists(path_ := os.path.join("app", "logs")):
        os.makedirs(path_, exist_ok=True)
    if not os.path.exists(file_ := os.path.join(path_, "main_logger.log")):
        with open(file_, "w"):
            pass
    config_path = os.path.join("app", "configuration", "logger_config.yaml")
    with open(config_path) as file:
        config = yaml.safe_load(file)
    logging.config.dictConfig(config)
