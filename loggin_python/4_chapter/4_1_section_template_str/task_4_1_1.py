import logging
import sys

# Настройка базовой конфигурации (не изменять)
logging.basicConfig(level=logging.INFO, stream=sys.stdout)


def log_server_event(event_type, timestamp):
    logging.info(f"Событие типа '{event_type}' произошло в {timestamp}")


# Примеры вызова функции
log_server_event("Ошибка подключения", "2024-09-03 11:00")
log_server_event("Успешное подключение", "2024-09-03 12:00")
