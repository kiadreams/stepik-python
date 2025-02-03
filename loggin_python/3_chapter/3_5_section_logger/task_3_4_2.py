import logging
import sys

# Настройка логгера
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Установите уровень логирования

#НЕОБХОДИМО ДЛЯ ТЕСТИРОВАНИЯ
####################################################################
console_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    '%(module)s - %(levelname)s - %(name)s - %(message)s',
) # Установите форматер
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
####################################################################

# Ваш код здесь (используйте logger)
logger.debug('This is a debug message')