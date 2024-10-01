from pprint import pprint


"""
LEGB — это аббревиатура, обозначающая порядок, в котором Python ищет имена
переменных, когда вы используете их в своем коде. Буквы означают:
    L (local) — локальная область видимости
    E (enclosing) — локальная область объемлющих функций
    G (global) — глобальная область видимости
    B (built-in) — встроенная
"""


def some(v, k):
    # СПИСОК ИМЕН ЛОКАЛЬНОГО ПРОСТРАНСТВА ВИДИМОСТИ ФУНКЦИИ
    print(dir())

    # ВЫВОД ПРОСТРАНСТВА ИМЕН ДЛЯ local() и global() в локальном пространстве
    pprint(globals())
    print()
    print(locals())
    return v, k


some(1, 1)
print()

age = 21


def print_age():
    new_age = 30
    print(age)


# СПИСОК ИМЕН ВСТРОЕННОГО ПРОСТРАНСТВА ВИДИМОСТИ (ИНТЕРПРЕТАТОРА)
print(dir(__builtins__), len(dir(__builtins__)))
print()

# СПИСОК ИМЕН ВСТРОЕННОГО ПРОСТРАНСТВА ВИДИМОСТИ (ИНТЕРПРЕТАТОРА)
print(dir(), len(dir()))
print()

# ВЫВОД ПРОСТРАНСТВА ИМЕН ДЛЯ local() и global() в глобальном пространстве
pprint(globals())
print()
pprint(locals())
print()


# ОБЪЕМЛЮЩЕЕ ПРОСТРАНСТВО ИМЁН - ФУНКЦИЯ С ВЛОЖЕННОЙ ФУНКЦИЕЙ
def outer_function():
    x = 15
    y = 10

    def inner_function():
        w = 40
        print(x + y + w)
        print("Доступные имена в inner_function", locals())

    inner_function()
    print("Доступные имена в outer_function", locals())


outer_function()
print()


def main_func():
    a = 1

    def inner_func():
        nonlocal a
        print("Печатаем a из inner_func", a)
        a += 1
        print("Печатаем a из inner_func", a)
        print("Печатаем b из inner_func", b)  # Вот тут будет ошибка NameError

    inner_func()
    b = 2
    print("Печатаем a из main_func", a)
    print("Печатаем b из main_func", b)


main_func()
print()
