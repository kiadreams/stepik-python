def gen_fibonacci_numbers(n):
    count = 0
    last_elem = curr_elem = 0
    next_elem = 1
    while count < n:
        count += 1
        yield next_elem
        last_elem, curr_elem = curr_elem, next_elem
        next_elem = last_elem + curr_elem


for i in gen_fibonacci_numbers(11):
    print(i)

print('Второй вариант'.center(100, '-'))


def gen_fibonacci_numbers(n):
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b


for i in gen_fibonacci_numbers(11):
    print(i)