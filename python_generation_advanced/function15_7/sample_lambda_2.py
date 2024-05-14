def generator_square_polynom_1(a, b, c):
    def square_polynom(x):
        return a*x**2 + b*x + c
    return square_polynom

# Такой код можно переписать так:

def generator_square_polynom(a, b, c):
    return lambda x: a*x**2 + b*x + c

# Этот пример показывает, что анонимные функции являются замыканиями: возвращаемая функция запоминает значения переменных a, b, c из внешнего окружения


# В теле анонимной функции не получится выполнить несколько действий и не получится использовать многострочные конструкции вроде циклов for и while. Однако можно использовать тернарный условный оператор.

numbers = [-2, 0, 1, 2, 17, 4, 5, 6]

result = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))

print(result, '\n')


# Как и обычные функции, определенные с помощью ключевого слова def , анонимные функции поддерживают все способы передачи аргументов:

#     - позиционные аргументы;
#     - именованные аргументы;
#     - переменный список позиционных аргументов (*args);
#     - переменный список именованных аргументов (**kwargs);
#     - обязательные аргументы (*).

f1 = lambda x, y, z: x + y + z
f2 = lambda x, y, z=3: x + y + z
f3 = lambda *args: sum(args)
f4 = lambda **kwargs: sum(kwargs.values())
f5 = lambda x, *, y=0, z=0: x + y + z


print(f1(1, 2, 3))
print(f2(1, 2))
print(f2(1, y=2))
print(f3(1, 2, 3, 4, 5))
print(f4(one=1, two=2, three=3))
print(f5(1))
print(f5(1, y=2, z=3), '\n')


result = list(map(lambda x: x.split(), ['a', 'a b', 'a b c']))

print(result)