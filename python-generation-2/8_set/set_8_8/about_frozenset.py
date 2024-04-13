my_set_1 = frozenset({1, 2, 3, 4})
my_set_2 = frozenset([1, 2, 3, 4, 5, 6, 7])
my_set_3 = frozenset('sfsdfsdjks')
my_set_4 = {1, 2, 3, 4}

print(my_set_1 == my_set_4)
print(my_set_1, my_set_2, my_set_3, '\n')


print(my_set_1 < my_set_2)
my_tuple_1 = my_set_1,
my_tuple_2 = my_set_4, {1, 2, 3}
print(my_tuple_1, my_tuple_2)
print(my_tuple_2[1:])
print(type(my_tuple_1), type(my_tuple_2))
my_set_4.discard(4)
print(my_tuple_1, my_tuple_2)
print(my_tuple_2, '\n')
my_set_5 = set()
my_set_5.add(my_set_1)
my_set_5.add(my_set_2)
print(my_set_5)
print('При добавлении в множество обычное множество, выдаст ошибку !!! при выполнении !!!:')
my_set_5.add(my_set_4)
print(my_set_5)
