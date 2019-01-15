
from loggingmodule import init_logging

class test_class:
    def __init__(self):
        logger = init_logging(__name__)

        logger.info("print info")
        logger.debug("print debug")


if __name__ == "__main__":
    test_class()
