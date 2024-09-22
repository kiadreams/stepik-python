def gen_fibonacci_numbers(n):
    x0 = 0
    x1 = 1
    for i in range(n):
        yield x1
        x0, x1 = x1, x1 + x0


for i in gen_fibonacci_numbers(10):
    print(i)