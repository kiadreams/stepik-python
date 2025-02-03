import logging.config
import yaml


# Загружаем конфигурацию из файла YAML
with open("logging.yml", "r") as f:
    config = yaml.safe_load(f)


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
