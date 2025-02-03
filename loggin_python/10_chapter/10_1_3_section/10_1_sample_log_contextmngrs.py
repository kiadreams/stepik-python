import logging
import time
from contextlib import contextmanager


# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@contextmanager
def log_execution_time():
    start_time = time.time()  # Запуск таймера
    yield
    end_time = time.time()  # Остановка таймера
    execution_time = end_time - start_time  # Вычисление времени выполнения
    logger.info(f"Код выполнен за {execution_time:.2f} секунд")


# Использование контекстного менеджера
with log_execution_time():
    # Имитация выполнения кода
    time.sleep(2)
