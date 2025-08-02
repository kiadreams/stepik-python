class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.log_level = 'INFO'
        return cls._instance

    @classmethod
    def set_level(cls, level: str):
        if cls._instance is None:
            raise ValueError('The instance has not created')
        cls._instance.log_level = level

    @staticmethod
    def get_logger():
        return Logger()


# Проверка работы кода--------------------------------------------------------
logger_1 = Logger.get_logger()
print(logger_1.log_level)  # Выведет "INFO"
Logger.set_level("DEBUG")
print(logger_1.log_level)  # Выведет "DEBUG"

logger_2 = Logger.get_logger()
print(logger_2.log_level)  # Выведет "DEBUG"
print(logger_2 is logger_1)