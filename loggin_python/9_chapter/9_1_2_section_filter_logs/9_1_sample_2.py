import logging


class TagFilter(logging.Filter):
    def __init__(self, tag):
        super().__init__()
        self.tag = tag

    def filter(self, record):
        return self.tag in record.msg


# Настройка логгера
logger = logging.getLogger("TaggedLogger")
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Добавление фильтра к обработчику
console_handler.addFilter(TagFilter("important"))

# Установка формата сообщений
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# Добавление обработчика в логгер
logger.addHandler(console_handler)

# Примеры записей
logger.debug("Это важное сообщение: important")
logger.info("Это обычное сообщение")
