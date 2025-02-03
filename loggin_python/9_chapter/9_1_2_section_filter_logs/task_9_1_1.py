import logging
import sys


class ErrorFilter(logging.Filter):
    def __init__(self):
        super().__init__()

    def filter(self, record):
        return record.levelno == logging.ERROR


# Создание логгера с именем error_logger
logger = logging.getLogger()
logger.setLevel(level=logging.DEBUG)

# Создание консольного хэндлера (обязательно укажите stream=sys.stdout)
cns_handler = logging.StreamHandler(stream=sys.stdout)
cns_handler.setLevel(level=logging.DEBUG)

# Добавление фильтра к обработчику
cns_handler.addFilter(ErrorFilter())

# Создание форматировщика в формате уровень - сообщение
cns_formatter = logging.Formatter("%(levelname)s - %(message)s")
cns_handler.setFormatter(cns_formatter)

# Добавление обработчика к логгеру
logger.addHandler(cns_handler)

# Примеры сообщений
logger.debug("Это сообщение отладки")
logger.error("Это сообщение об ошибке")
