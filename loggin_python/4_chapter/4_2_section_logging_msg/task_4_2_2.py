import logging
import sys

# Настройка базовой конфигурации (не изменять)
logging.basicConfig(level=logging.WARNING, stream=sys.stdout)


def check_value(value):
    # Ваш код
    if value < 10:
        logging.warning(f"Значение меньше 10: {value}")


check_value(int(input()))
