my_list = ['adfa', 'asfagfds', 'asdfas', 'jklj', 'jiiuuo']
my_dict = dict(enumerate(my_list))
print(my_dict)
print()

keys = ['name', 'age', 'job', 'adress']
values = ['Timur', 28, 'Teacher', 'Russia']
info = dict(zip(keys, values))
print(info)
print()

my_dict_2 = dict.fromkeys(keys, (5, 4))
print(my_dict_2)
print()

del my_dict_2['name']
print(my_dict_2)
print()
