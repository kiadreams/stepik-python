def func1(elem1, elem2, elem3):
    return elem1 + elem2 + elem3


numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30, 40, 50]
numbers3 = [100, 200, 300, 400, 500]

# преобразуем итератор в список
new_numbers = list(map(func1, numbers1, numbers2, numbers3))  
print(new_numbers, '\n')

# Если в последовательностях разное количество элементов, то последовательность с минимальным количеством элементов становится ограничителем.

def func2(elem1, elem2, elem3):
    return elem1 + elem2 + elem3


numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20]
numbers3 = [100, 200, 300, 400, 500]

# преобразуем итератор в список
new_numbers = list(map(func2, numbers1, numbers2, numbers3))  

print(new_numbers, '\n')

# !!! БОМБА !!!
# Приведем пример удобного использования встроенной функции map(), которой передано две последовательности.

circle_areas = [3.56773, 5.57668, 4.31914, 6.20241, 91.01344, 32.01213]

# округляем числа до 1 знака после запятой
result1 = list(map(round, circle_areas, [1]*6)) 

# округляем числа до 1,2,...,6 знаков после запятой
result2 = list(map(round, circle_areas, range(1, 7)))   

print(circle_areas)
print(result1)
print(result2)



# ПРИМЕР реализации функции map может выглядеть так:

def map(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)
    return result
