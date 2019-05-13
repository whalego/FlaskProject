# https://qiita.com/amedama/items/b856b2f30c2f38665701
# https://qiita.com/mimitaro/items/9fa7e054d60290d13bfc

import logging
from logging import getLogger, StreamHandler, Formatter

logger = None

def init_logging(name):
    global logger

    if logger is None:
        logger = getLogger(name)
    else:
        return logger

    logger.setLevel(logging.DEBUG)

    handler = StreamHandler()
    handler.setLevel(logging.INFO)

    h_format = Formatter("%(asctime)0.19s - %(module)s[%(levelname)s] %(funcName)s -> %(message)s ")
    handler.setFormatter(h_format)

    logger.addHandler(handler)

    # logger.info("start logging")

    return logger


if __name__ == "__main__":
    logger = init_logging(__name__)
    logger.info("print info")
    logger.debug("print debug")

