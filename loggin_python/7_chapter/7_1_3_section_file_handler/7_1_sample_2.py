import logging

# Создание логгера
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)  # Уровень логирования для этого обработчика

# Создание форматировщика и добавление его к обработчику
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)

# Логирование сообщений
logger.debug('Это сообщение уровня DEBUG')  # Не будет записано, так как уровень INFO
logger.info('Это сообщение уровня INFO')
logger.warning('Это сообщение уровня WARNING')
logger.error('Это сообщение уровня ERROR')
logger.critical('Это сообщение уровня CRITICAL')