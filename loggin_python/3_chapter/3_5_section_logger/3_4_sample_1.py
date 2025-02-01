import logging

# Создание объекта логгера
logger = logging.getLogger(__name__)

# Установка уровня логгирования
logger.setLevel(logging.DEBUG)

# Создание обработчика
handler = logging.StreamHandler()

# Создание форматтера
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Привязка форматтера к обработчику
handler.setFormatter(formatter)

# Привязка обработчика к логгеру
logger.addHandler(handler)

# Использование логгера для записи сообщений
logger.info("This is an informational message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")

# Завершение работы с логгером
logger.removeHandler(handler)
handler.close()
