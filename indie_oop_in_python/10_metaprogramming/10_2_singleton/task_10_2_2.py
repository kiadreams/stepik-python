from functools import wraps


# Реализуйте декоратор singleton
def singleton(cls):
    instance = None

    @wraps(cls)
    def wrapper(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance

    return wrapper


# Неправильная реализация...
# def singleton(cls):
#     instance = cls()
#     def inner():
#         return instance
#     return inner


@singleton
class Logger:
    def __init__(self, level):
        self.level = level
        print(f'вызван инит с уровнем {level}')


@singleton
class AppConfig:
    pass


@singleton
class SMTPServerConfig:
    pass


log = Logger('info')
app_conf = AppConfig()
app_conf_2 = AppConfig()
smtp_conf = SMTPServerConfig()
assert log is Logger()
log2 = Logger('debug')
print(log.level, log2.level)
assert app_conf is app_conf_2
assert smtp_conf is SMTPServerConfig()
assert log is not app_conf
assert log is not smtp_conf
assert app_conf is not smtp_conf
print('Good')
