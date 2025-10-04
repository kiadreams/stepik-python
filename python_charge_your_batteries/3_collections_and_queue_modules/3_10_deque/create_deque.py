from collections import deque

# Создаем пустой объект deque
empty_deque = deque()
print(empty_deque)  # deque([])

# создание дека на основании кортежа
print(deque((1, 2, 3, 4)))  # deque([1, 2, 3, 4])

# создание на основании списка
print(deque([1, 2, 3, 4], maxlen=2))  # deque([3, 4], maxlen=2)

# создание дека на основании range
print(deque(range(1, 5)))  # deque([1, 2, 3, 4])

# создание дека на основании строки
print(deque("abcd"))  # deque(['a', 'b', 'c', 'd'])

# создание дека на основании множества
print(deque({6, 3, 4, 4, 3, 5, 6}))  # deque([3, 4, 5, 6])

numbers = {"one": 1, "two": 2, "three": 3, "four": 4}
print(deque(numbers.keys()))  # deque(['one', 'two', 'three', 'four'])
print(deque(numbers.values()))  # deque([1, 2, 3, 4])
print(deque(numbers.items()))  # deque([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
