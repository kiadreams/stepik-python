import logging
import time
from functools import wraps

# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Запуск таймера
        result = func(*args, **kwargs)
        end_time = time.time()  # Остановка таймера
        execution_time = end_time - start_time  # Вычисление времени выполнения
        logger.info(
            f"Функция {func.__name__} выполнилась "
            f"за {execution_time:.2f} секунд",
        )
        return result

    return wrapper


@log_execution_time
def example_function():
    # Имитация выполнения функции
    time.sleep(2)


example_function()
