import logging
import sys

# Настройка базового конфигуратора
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    # filename="myapp.log", # Вывод в файл
    # stream=sys.stdout, # Вывод в поток вывода (консоль)
    # Вывод в поток вывода (консоль) с помощью обработчика
    handlers=[logging.StreamHandler(sys.stdout)],
)

# Создание логгера
logger = logging.getLogger("myapp")

# Запись сообщений
logger.debug("Это отладочное сообщение")
logger.info("Это информационное сообщение")
logger.warning("Это предупреждающее сообщение")
logger.error("Это сообщение об ошибке")
logger.critical("Это критическое сообщение")
