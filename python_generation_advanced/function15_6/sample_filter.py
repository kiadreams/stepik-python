def func1(elem):
    return elem >= 0


numbers = [-1, 2, -3, 4, 0, -20, 10]

# преобразуем итератор в список
positive_numbers = list(filter(func1, numbers))

print(positive_numbers, '\n')


# Встроенной функции filter() можно в качестве первого параметра func передать значение None. В таком случае каждый элемент последовательности будет проверен на соответствие значению True. Если элемент в логическом контексте возвращает значение False, то он не будет добавлен в возвращаемый результат.

my_list = [1, 0, 10, '', None, [], [1, 2, 3], ()]
true_values = filter(None, my_list)

for value in true_values:
    print(value)



# ПРИМЕР реализации функции filter может выглядеть так:

def filter(function, items):
    result = []
    for item in items:
        if function(item):        
            result.append(item)  # добавляем элемент item если функция function вернула значение True
    return result


