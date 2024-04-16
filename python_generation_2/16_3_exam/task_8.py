from operator import add, sub, mul, truediv


def arithmetic_operation(operation):
    functions = {'+': add, '-': sub, '*': mul, '/': truediv}
    return functions[operation]


add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))
