a = [['moskva',495], ['piter', 812], ['penza', 8412], [1, 2]]
cities = dict(a)
print(cities)
print(type(cities))

print()

print(person := dict(zip(['name', 'surname', 'age'], ['Vasya', 'Petrov', 25])))

print()

dict_1 = {'John': 15, 'Rick': 10, 'Misa' : 12 }
dict_2 = {'Bonnie': 18,'Rick': 20}
dict_3 = dict_1 | dict_2
dict_4 = dict_2 | dict_1
print(dict_3)
print('-'*15)
print(dict_4)