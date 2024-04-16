set_1 = {1, 2, 3, 4, 5, 6, 7}
set_2 = {1, 4, 5, 7}
set_3 = {1, 2, 3, 4, 5, 6, 7}
set_4 = {23, 34, 45}
print('Подмножество на операндах:')
print(set_2 <= set_1, set_2 < set_1)
print(set_3 <= set_1, set_3 < set_1)
print('\n', 'Подмножество на методах:')
print(set_2.issubset(set_1), set_2.issubset(set_1))
print(set_3.issubset(set_1), set_3.issubset(set_1))
print()
print('Надмножество в операндах:')
print(set_1 >= set_2, set_1 > set_2)
print(set_1 >= set_3, set_1 > set_3)
print('\n', 'Надмножество в методах:')
print(set_1.issuperset(set_2), set_1.issuperset(set_2))
print(set_3.issuperset(set_1), set_3.issuperset(set_1))
print()
print('Проверка на отсутствие общих элементов:')
print(set_1.isdisjoint(set_2), set_1.isdisjoint(set_3), set_1.isdisjoint(set_4))
print(set_2.isdisjoint(set_1), set_3.isdisjoint(set_1), set_4.isdisjoint(set_1))
