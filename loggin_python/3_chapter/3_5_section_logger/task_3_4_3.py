import logging
import sys

# Ваш код
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger()
logger.debug("This is an debug message.")
logger.info("This is an informational message.")
logger.warning("This is a warning message.")
