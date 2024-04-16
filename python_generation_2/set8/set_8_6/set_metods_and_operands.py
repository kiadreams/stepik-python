my_set_1 = {1, 2, 3, 4, 5, 6, 7}
my_set_2 = {4, 5, 6, 7, 8, 9, 0}

print('\n''Объединеие множеств:', end=' ')
print(my_set_1.union(my_set_2), ' or ', my_set_1 | my_set_2, '\n')

print('Пересечение множеств:', end=' ')
print(my_set_2.intersection(my_set_1), ' or ', my_set_1 & my_set_2, '\n')

print('Разность множеств:', end=' ')
print(my_set_1.difference(my_set_2), ' or ', my_set_1 - my_set_2, '\n')

print('Симметричная разность:', end=' ')
print(my_set_1.symmetric_difference(my_set_2), ' or ', my_set_1 ^ my_set_2, '\n')

print('\n', 'Методы, изменяющие исходное множество!', '\n', '\n')

print('Объединеие множеств:', end=' ')
my_set_1.update(my_set_2)
print(my_set_1, ' or ', end=' ')
my_set_1 = {1, 2, 3, 4, 5, 6, 7}
my_set_1 |= my_set_2
print(my_set_1, '\n')

print('Пересечение множеств:', end=' ')
my_set_1 = {1, 2, 3, 4, 5, 6, 7}
my_set_1.intersection_update(my_set_2)
print(my_set_1, ' or ', end=' ')
my_set_1 = {1, 2, 3, 4, 5, 6, 7}
my_set_1 &= my_set_2
print(my_set_1, '\n')


print('Разность множеств:', end=' ')
my_set_1 = {1, 2, 3, 4, 5, 6, 7}
my_set_1.difference_update(my_set_2)
print(my_set_1, ' or ', end=' ')
my_set_1 = {1, 2, 3, 4, 5, 6, 7}
my_set_1 -= my_set_2
print(my_set_1, '\n')

print('Симметричная разность:', end=' ')
my_set_1 = {1, 2, 3, 4, 5, 6, 7}
my_set_1.symmetric_difference_update(my_set_2)
print(my_set_1, ' or ', end=' ')
my_set_1 = {1, 2, 3, 4, 5, 6, 7}
my_set_1 ^= my_set_2
print(my_set_1, '\n')