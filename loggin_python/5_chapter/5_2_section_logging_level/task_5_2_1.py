import logging
import sys

# Настройка базовой конфигурации (не изменять)
logging.basicConfig(level=logging.ERROR, stream=sys.stdout)


def open_file(file_path):
    try:
        with open(file_path) as f:
            pass
    except FileNotFoundError as e:
        logging.error("Ошибка открытия файла: %s", e)


open_file("non_existent_file.txt")
