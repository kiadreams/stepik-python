from time import perf_counter, sleep


def timer():
    start = perf_counter()

    def inner():
        return perf_counter() - start

    return inner


q = timer()
sleep(1)  # делаем паузу в 1 секунду
print(q())
sleep(2)  # делаем паузу в 2 секунды
print(q())
sleep(3)  # делаем паузу в 3 секунды
print(q())
