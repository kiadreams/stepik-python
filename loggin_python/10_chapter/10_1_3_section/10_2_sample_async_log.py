import logging.handlers
from concurrent.futures import ThreadPoolExecutor


# Настройка асинхронного обработчика
class AsyncHandler(logging.Handler):
    def __init__(self, handler):
        super().__init__()  # Вызов конструктора родительского класса
        self.handler = handler  # Сохраняем переданный обработчик
        # Создаем пул потоков с одним рабочим потоком
        self.executor = ThreadPoolExecutor(max_workers=1)

    def emit(self, record):
        # Отправляем задачу на выполнение в пул потоков
        self.executor.submit(self.handler.emit, record)


# Настройка логгера
logger = logging.getLogger("AsyncLogger")
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи в файл
file_handler = logging.FileHandler("async.log")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Обертывание обработчика в асинхронный обработчик
async_handler = AsyncHandler(file_handler)
logger.addHandler(async_handler)

# Логирование сообщений
for i in range(100):
    logger.debug(f"Async message {i}")


"""
    Создание асинхронного обработчика (AsyncHandler):
        Класс AsyncHandler наследуется от logging.Handler и оборачивает 
        стандартный обработчик.
        В конструкторе __init__ принимается обычный обработчик (например, 
        FileHandler) и создается пул потоков с использованием 
        ThreadPoolExecutor. Этот пул будет использоваться для выполнения 
        задач логирования асинхронно.
        Метод emit переопределяется таким образом, чтобы задачи по записи 
        логов отправлялись в пул потоков. Это позволяет логировать сообщения 
        без блокировки основного потока приложения.

    Настройка логгера:
        Логгер AsyncLogger создается и настраивается на уровень DEBUG, чтобы 
        захватывать все сообщения от уровня DEBUG и выше.
        Создается FileHandler для записи сообщений в файл async.log. Форматтер 
        задает формат сообщений, включающий временную метку, уровень 
        логирования и само сообщение.
        Обычный FileHandler оборачивается в AsyncHandler, который обрабатывает 
        запись сообщений в фоновом потоке.

    Логирование сообщений:
        В цикле создаются 100 сообщений уровня DEBUG. Эти сообщения 
        обрабатываются асинхронно, что позволяет основному потоку приложения 
        продолжать свою работу без задержек, связанных с записью логов.
"""