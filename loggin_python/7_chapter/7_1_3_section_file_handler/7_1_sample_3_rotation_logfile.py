import logging
from logging.handlers import RotatingFileHandler

# Создание логгера
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Создание обработчика с ротацией файлов
rotating_handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=5)
rotating_handler.setLevel(logging.INFO)

# Создание форматировщика и добавление его к обработчику
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
rotating_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(rotating_handler)

# Логирование сообщений
for i in range(100):
    logger.info(f"Запись номера {i}")
