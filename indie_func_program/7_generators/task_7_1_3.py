def my_range_gen(n):
    yield from range(n)


for value in my_range_gen(5):
    print(value)