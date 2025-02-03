import logging

# Настройка базовой конфигурации логирования
logging.basicConfig(
    level=logging.DEBUG,  # Уровень логирования
    format="%(asctime)s - %(levelname)s - %(message)s",  # Формат сообщений
    handlers=[
        logging.FileHandler("app.log"),  # Запись в файл
        logging.StreamHandler(),  # Также вывод на консоль (опционально)
    ],
)

# Логирование сообщений
logging.debug("Это сообщение уровня DEBUG")
logging.info("Это сообщение уровня INFO")
logging.warning("Это сообщение уровня WARNING")
logging.error("Это сообщение уровня ERROR")
logging.critical("Это сообщение уровня CRITICAL")
