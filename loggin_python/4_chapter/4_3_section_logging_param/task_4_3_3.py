import logging
import sys

# Настройка базового логгера (не изменять)
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# Логирование добавления товара в корзину
logging.info("Товар добавлен в корзину: %s (цена: %s)", input(), input())
