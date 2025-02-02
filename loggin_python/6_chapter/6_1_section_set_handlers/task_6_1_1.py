import logging
import sys

# Создание логгера
logger = logging.getLogger('warning_logger')

# Создание консольного хэндлера (обязательно укажите stream=sys.stdout)
cls_handler = logging.StreamHandler(sys.stdout)
cls_handler.setLevel(logging.WARNING)

# Создание форматировщика
hand_formater = logging.Formatter('%(levelname)s - %(message)s')
cls_handler.setFormatter(hand_formater)

# Добавление хэндлера к логгеру
logger.addHandler(cls_handler)

# Пример логирования
logger.warning('Это предупреждение будет отображено')
