import logging
from logging import FileHandler, StreamHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = FileHandler('log_file.log', encoding='utf-8')
stream_handler = StreamHandler()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def division():
    logger.debug("Начало выполнения деления!")
    try:
        dividend = float(input("Введите делимое: "))
        divisor = float(input("Введите делитель: "))
        result = dividend / divisor
    except ValueError:
        logger.log(logging.CRITICAL, "Введены не числовые значения")
    except ZeroDivisionError:
        logger.error("Деление на ноль", exc_info=True)
    else:
        logger.info(f"Получен результат {dividend / divisor} в процессе деления {dividend} на {divisor}")
        return result


res = division()
print(res)
