import logging
import sys


# Создание логгера
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Создание консольного хэндлера (обязательно укажите stream=sys.stdout)
cns_handler = logging.StreamHandler(sys.stdout)
cns_handler.setLevel(logging.DEBUG)

# Создание форматировщика
cns_formater = logging.Formatter("%(levelname)s - %(message)s")
cns_handler.setFormatter(cns_formater)

# Добавление хэндлера к логгеру
logger.addHandler(cns_handler)

# Пример логирования
logger.debug("Это сообщение уровня DEBUG")
logger.info("Это информационное сообщение")
logger.warning("Это предупреждающее сообщение")
logger.error("Это сообщение об ошибке")
logger.critical("Это сообщение уровня CRITICAL")
