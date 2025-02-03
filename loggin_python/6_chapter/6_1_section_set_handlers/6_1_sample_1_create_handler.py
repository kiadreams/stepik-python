import logging

# Создание логгера
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования

# Создание консольного хэндлера
console_handler = logging.StreamHandler()
console_handler.setLevel(
    logging.INFO
)  # Устанавливаем уровень логирования для хэндлера

# Создание форматировщика
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)  # Применяем форматировщик к хэндлеру

# Добавление хэндлера к логгеру
logger.addHandler(console_handler)

# Пример логирования
logger.debug("Это сообщение уровня DEBUG")
logger.info("Это сообщение уровня INFO")
logger.warning("Это сообщение уровня WARNING")
