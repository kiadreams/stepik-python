def create_counter():
    count = 0

    def inner():
        pass

    def increment(value: int = 1):
        nonlocal count
        count += value
        return count

    def decrement(value: int = 1):
        nonlocal count
        count -= value
        return count

    inner.inc = increment
    inner.dec = decrement
    return inner


ex1 = create_counter()
print(ex1.inc(3))
print(ex1.inc(5))
print(ex1.inc(90))
print(ex1.dec(5))

ex2 = create_counter()
print(ex2.inc(1))
print(ex2.inc(2))
print(ex2.inc(23))
print(ex2.dec(10))