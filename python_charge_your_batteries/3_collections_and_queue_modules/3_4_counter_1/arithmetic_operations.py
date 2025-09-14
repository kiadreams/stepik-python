from collections import Counter

counter1 = Counter({'a': 2, 'b': 3, 'c': 1})
counter2 = Counter({'a': 1, 'b': 2, 'd': 4})

# Сложение
result = counter1 + counter2
print(result)
print()

# Вычитание
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

c3 = c1 - c2
print(c3)
print()

# Пересечение
counter1 = Counter({'a': 2, 'b': 3, 'c': 1})
counter2 = Counter({'a': 1, 'b': 2, 'd': 4})

result = counter1 & counter2
print(result)
print()

# Объединение
counter1 = Counter({'a': 2, 'b': 3, 'c': 1})
counter2 = Counter({'a': 1, 'b': 2, 'd': 4})

result = counter1 | counter2
print(result)
