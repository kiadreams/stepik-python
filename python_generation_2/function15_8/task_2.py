
func = lambda s: (s[0] + s[-1]).upper() == 'AA'

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))
print(func('a'))


