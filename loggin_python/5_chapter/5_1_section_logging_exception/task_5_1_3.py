import logging
import sys

# Настройка базовой конфигурации (не изменять)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)

try:
    int(input())
except ValueError as e:
    logging.error("Ошибка ввода: %s", e)
