import logging

# import psycopg2


class PostgreSQLHandler(logging.Handler):
    def __init__(self, db_config):
        super().__init__()
        self.db_config = db_config

    def emit(self, record):
        log_entry = self.format(record)
        self._write_log_to_db(record.levelname, log_entry)

    def _write_log_to_db(self, level, message):
        # Используем контекстный менеджер для соединения и курсора
        with psycopg2.connect(**self.db_config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO logs (level, message) VALUES (%s, %s)",
                    (level, message),
                )
                conn.commit()


"""
    PostgreSQLHandler(logging.Handler) — Создает класс PostgreSQLHandler, 
    который наследуется от logging.Handler. Это базовый класс для всех 
    обработчиков логов.
    
    __init__(self, db_config) — Конструктор класса, который принимает 
    конфигурацию базы данных db_config и вызывает конструктор родительского 
    класса.
    
    emit(self, record) — Метод, который вызывается для записи лог-сообщений. 
    Он форматирует запись с помощью self.format(record) и вызывает метод 
    _write_log_to_db для записи в базу данных.
    
    _write_log_to_db(self, level, message) — Метод, который устанавливает 
    соединение с базой данных PostgreSQL и выполняет SQL-запрос для вставки 
    записи в таблицу logs.
"""


db_config = {
    "dbname": "my_logs",
    "user": "your_username",
    "password": "your_password",
    "host": "localhost",
    "port": "5432",
}

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создание обработчика для PostgreSQL
db_handler = PostgreSQLHandler(db_config)
db_handler.setLevel(logging.DEBUG)

# Настройка формата логов
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
db_handler.setFormatter(formatter)

# Добавление обработчика в логгер
logger.addHandler(db_handler)

# Примеры лог-сообщений
logger.debug("Это сообщение уровня DEBUG")
logger.info("Это сообщение уровня INFO")
logger.warning("Это сообщение уровня WARNING")
logger.error("Это сообщение уровня ERROR")
logger.critical("Это сообщение уровня CRITICAL")
