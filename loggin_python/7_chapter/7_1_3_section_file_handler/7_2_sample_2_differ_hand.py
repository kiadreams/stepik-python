import logging

# Создание логгера
logger = logging.getLogger("multi_handler_logger")
logger.setLevel(logging.DEBUG)

# Файловый хэндлер
file_handler = logging.FileHandler("file.log")
file_handler.setLevel(logging.INFO)

# Консольный хэндлер
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Форматирование
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Добавление хэндлеров к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Запись логов
logger.debug("Отладочное сообщение")
logger.info("Информационное сообщение")
logger.warning("Предупреждение")
logger.error("Ошибка")
logger.critical("Критическая ошибка")
