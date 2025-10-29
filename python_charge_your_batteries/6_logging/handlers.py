import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(
    'log_file.log',
    maxBytes=100,
    backupCount=3,
    encoding='utf-8'
)
logger.addHandler(handler)


for i in range(50):
    logger.info(f'Информация {i}')
    logger.error(f'Ошибка {i}')
