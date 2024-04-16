dict_keys = {'1': '.,?!:', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
             '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ', '0': ' '}
string, result = input().upper(), ''

for i in string:
    for key, value in dict_keys.items():
        if i in value:
            result += key * (value.index(i) + 1)
print(result)
