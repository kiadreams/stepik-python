from functools import reduce
import operator


# !!! ИНТЕРЕСНО !!!
print((lambda x: (x + 3) * 5 / 2)(3), '\n')

# !!! ИНТЕРЕСНО !!!
result = list(filter(str.swapcase, ['a', '1', '', 'b', '2']))
print(result, '\n')

# !!! ИНТЕРЕСНО !!!
print(list(filter(None, ['', 1, 7, 'beegeek', None, False, 0])), '\n')

print(bool(None), '\n')

print(False == 0, False == '', False == None, False == [], '\n')


words = ['beegeek', 'stepik', 'python', 'iq-option']
result = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(result, '\n')


def flatten(data):
    return reduce(operator.concat, data, [])


result = flatten([[1, 2], [3, 4], [], [5]])
print(result, '\n')
