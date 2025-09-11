from collections import UserList

empty = UserList()
print(empty)
print(empty.data)

# Создание UserList из списка
ul_from_list = UserList([1, 2, 3, 4, 5])
print(ul_from_list)
print(ul_from_list.data)

# Создание UserList из кортежа
ul_from_tuple = UserList((6, 7, 8, 9, 10))
print(ul_from_tuple)
print(ul_from_tuple.data)

# Создание UserList из строки (каждый символ будет элементом списка)
ul_from_str = UserList("Hello")
print(ul_from_str)
print(ul_from_str.data)

# Создание UserList из другого объекта UserList
ul_from_user_list = UserList(UserList([11, 12, 13, 14, 15]))
print(ul_from_user_list)
print(ul_from_user_list.data)

# Создание UserList из диапазона чисел
ul_from_range = UserList(range(5))
print(ul_from_range)
print(ul_from_range.data)
