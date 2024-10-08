def average_numbers():
    summa = 0
    count = 0

    def inner(number):
        nonlocal summa, count
        summa = summa + number
        count = count + 1
        return summa / count

    return inner


r1 = average_numbers()
r2 = average_numbers()
print(r1(5))
print(r1(10))
print(r2(15))


def add(a, b):
    return a + b

def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'функция {func.__name__} вызывалась {count} раз')
        return func(*args,**kwargs)

    return inner
q = counter(add)

q(10, 20)
q(2,5)