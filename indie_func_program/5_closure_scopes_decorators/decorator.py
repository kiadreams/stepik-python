def decorator(func):
    def inner():
        print('Стартуем декоратор')
        func()
        print('Заканчиваем декоратор')

    return inner


@decorator
def say_hello():
    print('hello world')


@decorator
def say_bye():
    print('bye world')


say_hello()
print('--------')
say_bye()