import logging

logging.basicConfig(level=logging.ERROR)
my_logger = logging.getLogger("my_logger")


my_logger.debug("Это сообщение уровня DEBUG")
my_logger.info("Это сообщение уровня INFO")
my_logger.warning("Это сообщение уровня WARNING")
my_logger.error("Это сообщение уровня ERROR")
my_logger.critical("Это сообщение уровня CRITICAL")

my_logger.setLevel(logging.INFO)
my_logger.info("INFO Изменили уровень логирования")

my_logger.debug("Это сообщение уровня DEBUG - его все еще не видно")
my_logger.info("Это сообщение уровня INFO")
my_logger.warning("Это сообщение уровня WARNING")
my_logger.error("Это сообщение уровня ERROR")
my_logger.critical("Это сообщение уровня CRITICAL")
