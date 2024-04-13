def add3(x):
    return x + 3


def mul7(x):
    return x * 7


def compose(func_1, func_2):
    return lambda x: func_1(func_2(x))


print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))
