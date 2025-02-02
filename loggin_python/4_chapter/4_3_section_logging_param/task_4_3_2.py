import logging
import sys

# Настройка базового логгера (не изменять)
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

logging.info("Количество элементов в списке: %d", len(input().split()))
