#-------------------- СОЗДАНИЕ И ЗАПУСК КОРУТИНЫ!!!------------------------
print('СОЗДАНИЕ И ЗАПУСК КОРУТИНЫ'.center(100, '-'))
def coroutine():
    """
    обратите внимание, оператор yield используется
    как в традиционном смысле генератора,
    так и в смысле сопрограммы
    """
    print("Start")
    msg = yield  # указание получения данных
    yield msg.upper()  # возврат данных из генератора
    print("Finish")


coro = coroutine()  # создаем генератор

# поскольку сопрограмма является генератором
# код внутри не будет выполняться, пока не вызовем функцию next

next(coro)  # после этого перемещаемся к первому yield внутри функции-генератора

# метод .send() позволяет отправлять данные в сопрограмму
# это отправляет "hello" в первый yield
# поэтому переменной msg внутри coroutine будет присвоено это значение
result = coro.send("hello")

# Но наша сопрограмма также сразу сгенерирует msg.upper()
# Значит, в result сохранится это значение
print(result)  # HELLO

# next(coro) # Finish и затем StopIteration

"""
Когда вы вызываете next(coro), вы тем самым заставляете генератор возобновить
или начать свою работу и выполняться до первого встречного оператора yield.
Вызов метода .send() делает тоже самое: он активирует генератор в том месте,
где он прервал свою работу, и заставляет его выполнить свой код до следующей
инструкции yield. К тому же метод .send() дополнительно явно подставляет
переданное значение в место, где возобновляется работа генератора.
"""
print('ИНИЦИАЛИЗАЦИЯ КОРУТИНЫ'.center(100, '-'))


def infinity_coro():
    print("Запускаем нашу корутину!")
    while True:
        value = yield
        print('Передано значение', value)


#---------------------Первый вариант инициализации корутины!!!----------------
coro = infinity_coro()
print(coro)
next(coro) # Инициализация корутины
coro.send('Hi')
coro.send(100)

print()

#----------------- Второй способ инициализации корутины!!!-------------------
coro = infinity_coro()
coro.send(None) # Инициализация корутины
coro.send('Hi')
coro.send(100)

print('ТОЛЬКО NEXT, БЕЗ ПЕРЕДАЧИ ЗНАЧЕНИЙ КОРУТИНЕ'.center(100, '-'))
#-------------- ТОЛЬКО NEXT, БЕЗ ПЕРЕДАЧИ ЗНАЧЕНИЙ КОРУТИНЕ!!!-------------------

"""
Но оператор yield обладает двойственным поведением: даже если вы не передаёте
значение корутине через send, а просто продолжите работу функции через next,
оператор yield всегда будет подставлять значение None
"""
coro = infinity_coro()
next(coro)
next(coro)

print('ТОЛЬКО YIELD, БЕЗ ВОЗВРАТА ЗНАЧЕНИЙ ИЗ КОРУТИНЫ'.center(100, '-'))
#-------------- ТОЛЬКО NEXT, БЕЗ ПЕРЕДАЧИ ЗНАЧЕНИЙ КОРУТИНЕ!!!-------------------
"""
Аналогичная ситуации будет, когда yield используется только для получения
данных. В таком случае yield передает None вызывающей стороне как в примере 
ниже:
"""


def coroutine():
    value = yield
    print(f'Получено значение = {value}')


coro = coroutine()
value_from_coro = next(coro)  # Получаем значение None из корутины
print(value_from_coro)  # Печатает None
# next(coro)  # StopIteration

print('ВОЗВРАТ ЗНАЧЕНИЯ КОРУТИНОЙ ДО ПЕРЕДАЧИ ЕЙ'.center(100, '-'))
#-------------- ВОЗВРАТ ЗНАЧЕНИЯ КОРУТИНОЙ ДО ПЕРЕДАЧИ ЕЙ!!!-------------------


def coroutine():
    msg = yield "World"
    yield msg.upper()


coro = coroutine()

print(next(coro))  # World
result = coro.send("hello")
print(result)  # HELLO

print()

print('ОДНОВРЕМЕННЫЙ ПРИЁМ И ОТПРАВКА ЗНАЧЕНИЙ!!!'.center(100, '-'))
#----------------ОДНОВРЕМЕННЫЙ ПРИЁМ И ОТПРАВКА ЗНАЧЕНИЙ!!!--------------------


def coroutine():
    value = 0
    while True:
        received = yield value ** 2
        value = value if received is None else received
        print(f'Получено значение = {received}, отправлено {value ** 2}')


coro = coroutine()
value_from_coro = next(coro)
print('Получено при инициализации', value_from_coro)
value_from_coro = next(coro)
print('Получено на следующей итерации без передачи значения', value_from_coro)
value_from_coro = coro.send(1)
print('Получено после 1й отправки', value_from_coro)
value_from_coro = coro.send(2)
print('Получено после 2й отправки', value_from_coro)
value_from_coro = coro.send(3)
print('Получено после 3й отправки', value_from_coro)
value_from_coro = coro.send(4)
print('Получено после 4й отправки', value_from_coro)
value_from_coro = coro.send(5)
print('Получено после 5й отправки', value_from_coro)
coro.close()
