import logging


class LevelFilter(logging.Filter):
    def filter(self, record):
        return record.levelno >= logging.WARNING


class MessageFilter(logging.Filter):
    def filter(self, record):
        return "critical" in record.msg


# Настройка логгера
logger = logging.getLogger("ComplexLogger")
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи в файл
file_handler = logging.FileHandler("complex.log")
file_handler.setLevel(logging.DEBUG)

# Добавление фильтров к обработчику
file_handler.addFilter(LevelFilter())
file_handler.addFilter(MessageFilter())

# Установка формата сообщений
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавление обработчика в логгер
logger.addHandler(file_handler)

# Примеры записей
logger.info("Это обычное сообщение")
logger.warning("Это критическое сообщение")
logger.error("Это сообщение с критическим уровнем  critical")
