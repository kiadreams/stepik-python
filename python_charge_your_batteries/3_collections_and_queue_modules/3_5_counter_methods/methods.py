from collections import Counter


"""
Метод .elements() возвращает итератор с элементами, повторенными столько раз,
сколько раз они встречаются в объекте Counter
"""
words = ['Donald', 'Mickey', 'Donald', 'Mickey', 'Mickey']
names = Counter(words)
print(names)
print(names.elements(), *names.elements())
print()

"""
Метод most_common([n]): возвращает список n самых часто встречающихся элементов
и их количество в порядке убывания.
"""
c = Counter("abracadabra")
print(c.most_common(3))
print(c.most_common(None))
print()

"""
Метод .total() вычисляет сумму значений всех счетчиков по всем ключам у
экземпляра.
"""
a = Counter(a=10, b=7, c=1)
print(a)
print(a.total())
print()

"""
Метод subtract([iterable-or-mapping]): вычитает элементы из объекта Counter
на основе другого итерируемого объекта или словаря. При этом значения счетчиков
могут обнулится либо уйти в отрицательные значения.
"""
c1 = Counter("hello")
c2 = Counter("world")
c1.subtract(c2)
print(c1)
print()

"""
Метод fromkeys(iterable, v=None). Данный метод переопределен с единственной
целью вызывать исключение:
NotImplementedError('Counter.fromkeys() is undefined.
Use Counter(iterable) instead.')
"""

"""
Метод update([iterable-or-mapping]) используется для обновления счетчика
элементами из других итерируемых объектов или других объектов Counter. Метод
.update в обычном словаре заменяет значение ключа, а в объекте Counter он не
заменяет значение, а добавляет к количеству.
"""
c = Counter('which')
print(c)
c.update('witch') # добавляем элементы из строки
print(c)

d = Counter('watch')
c.update(d) # добавляем элементы из другого counter
print(c)
