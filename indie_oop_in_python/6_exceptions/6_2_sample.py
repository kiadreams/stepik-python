# Распространение исключений!!!
import

def third():
    print("старт третьей функции")
    1 / 0
    print("конец третьей функции")

def second():
    print("старт второй функции")
    # try:
    third()
    # except ZeroDivisionError as err:
    #     print("handling second")
    print("конец второй функции")


def first():
    print("старт первой функции")
    try:
        second()
    except ZeroDivisionError as err:
        print("handling first")
    print("конец первой функции")


print("начало main")
try:
    first()
except ZeroDivisionError as err:
    print("handling main")
print("конец main")