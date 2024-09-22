a = [ 10, 20, 30, 40]
print(enumerate(a))

print(list(enumerate(a)))
print()

words = ['variation', 'random', 'electronics', 'competence', 'collapse']
for index, value in enumerate(words):
    print(index, value)
print('-' * 15)
for index, value in enumerate(words, start=10):
    print(index, value)