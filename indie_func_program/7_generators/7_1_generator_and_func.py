import sys


def generate_even(limit):
    i = 0
    while i <= limit:
        yield i
        i += 2


def get_even(limit):
    i = 0
    values = []
    while i <= limit:
        values.append(i)
        i += 2
    return values


MAX_COUNT = 1000000

gen_obj = generate_even(MAX_COUNT)
usual_list = get_even(MAX_COUNT)

print(sys.getsizeof(gen_obj))  # 104
print(sys.getsizeof(usual_list))  # 4167352

print()

def get_colors():
    print('Red')
    yield 'Yellow'
    print('Black')
    yield 'Green'
    print('Gray')


gen_iter = get_colors()
print(next(gen_iter))
print(next(gen_iter))
# print(next(gen_iter)) Появляется исключение

print()


def get_colors():
    print('Red')
    yield 'Yellow'
    print('Black')
    return 'Green'
    print('Gray')

result = get_colors()
next(result)
print(next(result))  #  При return значение не возвращается, но срабатывфает
# ошибка StopIteration
