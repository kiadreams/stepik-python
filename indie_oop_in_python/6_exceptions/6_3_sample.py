# обработка исключений

try:
    # int("hello")
    # 1 / 0
    print("123")
    # a+b
except (ValueError, ZeroDivisionError) as err:
    print(f"handing ValueError {type(err)}")
else:
    print("Всё ок!!!")
finally:
    print("Это ВСЁ равно нужно сделать!!!")

print()

try:
    assert 1 == 2, "Что-то пошло не так"
except AssertionError as e:
    print("Отловили AssertionError:", e)
finally:
    print("Досвидули")

print()


d = {'name': 'Alex', 'surname': 'Petrov'}
try:
    print(d['Surname'])
except IndexError:
    print("Неправильный ключ")
finally:
    print("До скорой встречи")