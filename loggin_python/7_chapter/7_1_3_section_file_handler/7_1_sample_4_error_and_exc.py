import logging

logging.basicConfig(
    filename='errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    x = 1 / 0
except ZeroDivisionError:
    logging.error('Произошла ошибка деления на ноль', exc_info=True)

# ВТОРОЙ ВАРИАНТ РЕАЛИЗАЦИИ БОЛЕЕ ПРАВИЛЬНЫЙ...
try:
    x = 1 / 0
except ZeroDivisionError:
    logging.exception('Произошла ошибка деления на ноль')