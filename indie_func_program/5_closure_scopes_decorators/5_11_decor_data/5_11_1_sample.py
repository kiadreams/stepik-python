def dec(fn):
    print("Запуск декоратора")

    def wrapper(*args, **kwargs):
        print("Запуск inner")
        return fn(*args, **kwargs)

    return wrapper


@dec
def say_hello():
    return "Hello"


print(say_hello())
print(say_hello())
print(say_hello())
