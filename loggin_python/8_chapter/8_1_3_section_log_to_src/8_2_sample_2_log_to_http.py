import logging
import requests
import json


class HTTPLogHandler(logging.Handler):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def emit(self, record):
        log_entry = self.format(record)
        payload = {"level": record.levelname, "message": log_entry}
        try:
            response = requests.post(
                self.url,
                data=json.dumps(payload),
                headers={"Content-Type": "application/json"},
            )
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to send log: {e}")


# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

http_handler = HTTPLogHandler("https://remote-log-server/api/logs")
http_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
http_handler.setFormatter(formatter)

logger.addHandler(http_handler)

# Пример логирования
logger.debug("Debug message")
logger.info("Information message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")


"""
    HTTPLogHandler: Отправляет лог-сообщения на удалённый сервер через 
    HTTP POST запросы.
    requests.post(): Выполняет HTTP POST запрос для отправки логов.
"""