import logging
import logging.config
import json

# Загружаем конфигурацию из файла JSON
with open("logging.json", "r") as f:
    config = json.load(f)


# Применяем конфигурацию
logging.config.dictConfig(config)

# Получаем корневой логгер
logger = logging.getLogger()

# Примеры сообщений
logger.debug(
    "This is a debug message"
)  # Отфильтровано, так как уровень DEBUG < WARNING
logger.warning(
    "This is a warning message"
)  # Записано, так как уровень WARNING
logger.error("This is an error message")  # Записано, так как уровень ERROR
