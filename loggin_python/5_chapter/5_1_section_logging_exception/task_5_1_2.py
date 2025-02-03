import logging
import sys

# Настройка базовой конфигурации (не изменять)
logging.basicConfig(
    level=logging.ERROR,
    format="%(levelname)s - %(message)s",
    stream=sys.stdout,
)


def open_file(file_path):
    try:
        with open(file_path) as f:
            pass
    except FileNotFoundError as e:
        logging.error("Файл не найден: %s", e)


# Вызов функции (не изменять)
open_file("non_existent_file.txt")
