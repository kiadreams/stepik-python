# Функции all() и any() могут быть полезны в комбинации с функцией map(), которая может преобразовывать элементы последовательности (итерируемого объекта) к значению True/False в соответствии с неким условием.
numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]

result = all(map(lambda x: True if x > 10 else False, numbers))

if result:
    print('Все числа больше 10')
else:
    print('Хотя бы одно число меньше или равно 10')
print()

# То же самое, только упростив:
result_2 = all(map(lambda x: x > 10, numbers))
if result_2:
    print('Все числа больше 10')
else:
    print('Хотя бы одно число меньше или равно 10')
print()


numbers = [17, 91, 78, 55, 231, 45, 5, 89, 99, 11, 19]

result = any(map(lambda x: x % 2 == 0, numbers))
if result:
    print('Хотя бы одно число четное')
else:
    print('Все числа нечетные')
