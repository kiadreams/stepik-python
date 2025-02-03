import logging
import watchtower

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Используем with для создания и автоматического закрытия обработчика
with watchtower.CloudWatchLogHandler(
    log_group="my-log-group"
) as cloudwatch_handler:
    cloudwatch_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    cloudwatch_handler.setFormatter(formatter)

    logger.addHandler(cloudwatch_handler)

    # Пример логирования
    logger.debug("Debug message")
    logger.info("Information message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")

"""
watchtower — библиотека для отправки логов в AWS CloudWatch.
with watchtower.CloudWatchLogHandler(): Создаёт обработчик для CloudWatch и 
автоматически закрывает его после завершения блока кода.
"""
