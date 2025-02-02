import logging
import sys


# Настройка базовой конфигураци (не изменять)
logging.basicConfig(level=logging.ERROR, stream=sys.stdout)


def convert_temperature(celsius_str):
    try:
        print((float(celsius_str) * 9 / 5) + 32)
    except ValueError as e:
        logging.error("Ошибка преобразования температуры: %s", e)


# Вызов функции (не изменять)
convert_temperature(input())
