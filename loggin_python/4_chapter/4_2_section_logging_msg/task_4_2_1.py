import logging
import sys

# Настройка базовой конфигурации (не изменять)
logging.basicConfig(level=logging.INFO, stream=sys.stdout)


def add(a, b):
    # Ваш код
    logging.info(f"Вызвана функция {add.__name__} с параметрами a={a}, b={b}")
    add_res = a + b
    logging.info(f"Результат сложения: {add_res}")
    return add_res


# Вызов функции
add(int(input()), int(input()))
