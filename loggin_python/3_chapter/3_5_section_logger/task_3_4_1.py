import logging
import sys

# Настройка логгера
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Установите уровень логирования

#НЕОБХОДИМО ДЛЯ ТЕСТИРОВАНИЯ НЕ ИЗМЕНЯТЬ
####################################################################
console_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
####################################################################

# Ваш код здесь (используйте logger)
logger.info('This is an informational message')
