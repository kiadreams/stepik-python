import math

def choose_func(name, num):
    functions = dict(квадрат=num ** 2, куб=num ** 3, корень=num ** 0.5,
                     модуль=abs(num), синус=math.sin(num))
    if name in functions:
        return functions[name]

number, name_func = int(input()), input()
print(choose_func(name_func, number))