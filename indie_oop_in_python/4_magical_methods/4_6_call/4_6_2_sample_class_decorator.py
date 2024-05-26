# Например, у вас есть функция upload_file
def upload_file():
    print("Загрузка файла....")


# Создаем декоратор connect_storage
def connect_storage(func):
    def wrapper(*args, **kwargs):
        print("Подключение к хранилищу")
        func(*args, **kwargs)
        print("Отключение от хранилища")

    return wrapper


# Декорируем начальную функцию upload_file так
upload_file = connect_storage(upload_file)

# # или можно через символ @
# @connect_storage
# def upload_file():
#     print("Загрузка файла....")


# Функцию-декоратор можно легко заменить классом-декоратором, поскольку
# метод __call__ делает экземпляр класса вызываемым.
class Storage:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Подключение к хранилищу")
        self.func()
        print("Отключение от хранилища")


@Storage
def upload_file_1():
    print("Загрузка файла....")


if __name__ == "__main__":
    print("Работает декоратор - функция...")
    upload_file()
    print()
    print("Работает декоратор - класс...")
    upload_file_1()
