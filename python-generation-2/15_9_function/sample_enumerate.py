# Встроенная функция enumerate() возвращает кортеж из индекса элемента и самого элемента переданной ей последовательности (итерируемого объекта).
# Сигнатура функции следующая: enumerate(iterable, start). В качестве iterable может выступать любой итерируемый объект:
#  - список;
#  - кортеж;
#  - строка;
#  - множество;
#  - словарь и т.д.

# С помощью необязательного параметра start можно задать начальное значение индекса. По умолчанию значение параметра start = 0, то есть счет начинается с нуля.

colors = ['red', 'green', 'blue']

for pair in enumerate(colors):
    print(pair)
print(dict(enumerate(colors)))
