from collections import UserDict


# Создание пустого UserDict
user_dict = UserDict()
print(user_dict)
print(user_dict.data)
print('-' * 30)

# Создание непустого UserDict
d = {'a':1, 'b': 2, 'c': 3}
user_dict_1 = UserDict(d)
print(user_dict_1)
print(user_dict_1.data)

print('-'*30)

user_dict_2 = UserDict(a=100, w=200)
print(user_dict_2)
print(user_dict_2.data)
