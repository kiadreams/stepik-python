import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error("Произошла ошибка: %s", e, exc_info=True)
