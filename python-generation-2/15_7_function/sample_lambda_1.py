from functools import reduce


numbers = [1, 2, 3, 4, 5, 6]

new_numbers1 = list(map(lambda x: x+1, numbers))      #  увеличиваем на 1
new_numbers2 = list(map(lambda x: x*2, numbers))      #  удваиваем
new_numbers3 = list(map(lambda x: x**2, numbers))     #  возводим в квадрат

print(new_numbers1)
print(new_numbers2)
print(new_numbers3, '\n')


strings = ['a', 'b', 'c', 'd', 'e']
numbers = [3, 2, 1, 4, 5]

new_strings = list(map(lambda x, y: x*y, strings, numbers))

print(new_strings, '\n')


words = ['python', 'stepik', 'beegeek', 'iq-option']

new_words1 = list(filter(lambda w: len(w) > 6, words))    #  слова длиною больше 6 символов
new_words2 = list(filter(lambda w: 'e' in w, words))      #  слова содержащие букву e

print(new_words1)
print(new_words2, '\n')


words = ['python', 'stepik', 'beegeek', 'iq-option']
numbers = [1, 2, 3, 4, 5, 6]

summa = reduce(lambda x, y: x + y, numbers, 0)
product = reduce(lambda x, y: x * y, numbers, 1)
sentence = reduce(lambda x, y: x + ' loves ' + y, words, 'Everyone')

print(summa)
print(product)
print(sentence, '\n')
