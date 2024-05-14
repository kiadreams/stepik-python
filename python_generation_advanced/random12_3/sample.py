import random


n = 10000000
k = 0
s0 = 16
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)

    if y**3 - 2 * x**2 <= -1 and 2 * y + x**3 <= 3:
        k += 1

print((k / n) * s0)
