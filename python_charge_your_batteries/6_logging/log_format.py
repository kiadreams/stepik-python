import logging


log_format = "%(asctime)s::%(levelname)s::" "%(filename)s**%(lineno)d**%(message)s"

logging.basicConfig(level="DEBUG", format=log_format)


logging.debug("Debug message")

logging.info("Informative message")

logging.error("Error message")

