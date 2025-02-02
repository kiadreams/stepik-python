import logging
import sys

# Настройка базовой конфигурации
logging.basicConfig(level=logging.ERROR, stream=sys.stdout)


def convert_to_int(value):
    # Ваш код
    try:
        return int(value)
    except ValueError:
        logging.error(f'Ошибка преобразования: "{value}" не является числом.')


convert_to_int(input())
