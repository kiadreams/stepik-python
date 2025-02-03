

import logging

class ErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR

# Настройка логгера
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи в файл
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# Добавление фильтра к обработчику
file_handler.addFilter(ErrorFilter())

# Установка формата сообщений
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика в логгер
logger.addHandler(file_handler)

# Примеры записей
logger.debug('Это сообщение отладки')
logger.error('Это сообщение об ошибке')
