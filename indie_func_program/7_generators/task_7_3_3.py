def get_average():
    count = 0
    summa = yield
    while True:
        count += 1
        summa += yield summa / count


coro = get_average()
next(coro)
print(coro.send(10))
print(coro.send(20))
print(coro.send(6))
