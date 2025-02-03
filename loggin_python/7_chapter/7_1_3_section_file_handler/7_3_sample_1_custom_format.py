import logging


class CustomFormatter(logging.Formatter):
    def format(self, record):
        log_message = super().format(record)
        # Добавить кастомные детали
        return f"LOG: {log_message}"


# Создание логгера
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Создание файлового хэндлера
file_handler = logging.FileHandler("custom.log")
file_handler.setLevel(logging.DEBUG)

# Создание пользовательского форматировщика
formatter = CustomFormatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавление хэндлера к логгеру
logger.addHandler(file_handler)

# Пример логирования
logger.info("Это кастомное сообщение уровня INFO")
