from time import perf_counter


class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f"Вызывается функция {self.fn.__name__}")
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f"Функция {self.fn.__name__} отработала за {finish - start}")
        return result


# Полное декорирование...
@Timer
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr


@Timer
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_1(n):
    if n <= 2:
        return 1
    return fib_1(n - 1) + fib_1(n - 2)


fact(20)
print("\n")
print("Полное декорирование рекурсивной функции вызывает проблему...\n")
fib(3)
print("\n")
print("Реализация неполного декорирования рекурсивных функций...")
print("Декорируется только её вызов, но не сама функция...\n")
Timer(fib_1)(3)
