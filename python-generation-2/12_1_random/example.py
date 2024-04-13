import random

for _ in range(10):
    print(random.randint(1, 10))
print()
print(random.randrange(23))
print()
print(random.random())
print()
for _ in range(10):
    print(random.uniform(0.1, 99.9))
print()

# Явно устанавливаемое начальное число для получения псевдослучайных одинаковых последовательностей!
random.seed(17)
for _ in range(3):
    print(random.randint(1, 100))
print()
for _ in range(3):
    print(random.randint(1, 100))

