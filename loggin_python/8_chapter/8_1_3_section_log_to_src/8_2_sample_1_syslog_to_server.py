import logging
import logging.handlers

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Настройка обработчика Syslog
syslog_handler = logging.handlers.SysLogHandler(
    address=("remote-syslog-server", 514)
)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
syslog_handler.setFormatter(formatter)

logger.addHandler(syslog_handler)

# Пример логирования
logger.debug("Debug message")
logger.info("Information message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

"""
    SysLogHandler: Отправляет лог-сообщения на удалённый сервер через протокол 
    Syslog.
    address=('remote-syslog-server', 514): Адрес и порт удалённого Syslog 
    сервера.
"""
