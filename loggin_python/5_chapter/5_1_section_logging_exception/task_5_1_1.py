import logging
import sys

# Настройка базовой конфигурации (не изменять)
logging.basicConfig(
    level=logging.ERROR,
    format='%(levelname)s - %(message)s',
    stream=sys.stdout
)

def divide_numbers(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        logging.error('Ошибка деления: %s', e)

# Попытка деления на ноль
divide_numbers(int(input()), int(input()))