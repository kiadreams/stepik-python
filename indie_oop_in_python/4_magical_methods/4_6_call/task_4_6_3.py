import time


class Timer:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.function(*args, **kwargs)
        end = time.time()
        print(
            f"Функция {self.function.__name__} отрабоатала за "
            f"{end - start} секунд",
        )
        return result


@Timer
def calculate():
    for i in range(10000000):
        2**100


print(type(calculate))
print(calculate())
