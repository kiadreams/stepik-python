import random

n = int(input())    # количество попыток
for _ in range(n):
    print(('Орел', 'Решка')[random.randint(0, 1)])