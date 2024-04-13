import random

length = int(input())    # длина пароля
result = []
for _ in range(length):
    if random.randint(0, 1):
        result.append(chr(random.randint(65, 90)))
    else:
        result.append(chr(random.randint(97, 122)))
print(''.join(result))