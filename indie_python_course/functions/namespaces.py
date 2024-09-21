"""
Всего в python существует 4 вида пространства имен:

    builtins (встроенное пространство имен)
    global (глобальное пространство имен)
    enclosing (объемлющее пространство имен)
    local (локальное пространство имен)

При поиске переменных, Python использует правило LEGB. LEGB — это аббревиатура,
 обозначающая порядок, в котором Python ищет имена переменных,
  когда вы используете их в своем коде. Буквы означают:

    L (local) — локальная область видимости
    E (enclosing) — локальная область объемлющих функций
    G (global) — глобальная область видимости
    B (built-in) — встроенная

"""

# Встроенное пространство имен (built-in namespace)
print(dir(__builtins__))
print()


# _________________________________________________________________________

age = 21


def print_age():
    print(age)


print_age()  # prints 21
# Глобальное пространство имен (global namespace)
print(globals())
print()

# ____________________________________________________________________________

name = "Misha"


def print_age():
    age = 21
    name = "Ivan"
    print(age)
    # Локальное пространство имен (local namespace)
    print(locals())


def foo():
    x, y = 10, 20
    # Локальное пространство имен (local namespace)
    print(locals())


print_age()
foo()
print()

# ___________________________________________________________________________


# Объемлющее пространство имен
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


"""

Кроме того, вложенная функция может обращаться к нелокальным переменным 
объемлющей функции и изменять их. Для этого необходимо использовать
ключевого слова nonlocal

"""


def outer_function():
    x = 5

    def inner_function():
        nonlocal x
        x += 1
        print("внутри inner_function", x)

    print("внутри outer_function до inner_function", x)
    inner_function()
    print("внутри outer_function после inner_function", x)


outer_function()
