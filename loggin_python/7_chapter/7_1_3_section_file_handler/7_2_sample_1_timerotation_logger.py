import logging
from logging.handlers import TimedRotatingFileHandler

# Создание логгера
logger = logging.getLogger("example_logger")
logger.setLevel(logging.DEBUG)

# Создание хэндлера с ротацией по времени
timed_handler = TimedRotatingFileHandler(
    "timed_example.log", when="midnight", interval=1, backupCount=7
)
timed_handler.setLevel(logging.INFO)

# Настройка формата сообщений
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
timed_handler.setFormatter(formatter)

# Добавление хэндлера к логгеру
logger.addHandler(timed_handler)

# Запись логов
logger.info("Информационное сообщение")
