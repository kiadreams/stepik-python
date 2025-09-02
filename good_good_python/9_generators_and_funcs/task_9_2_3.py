import random

from string import ascii_lowercase, ascii_uppercase

# установка зерна датчика случайных чисел (не менять)
random.seed(1)


# здесь продолжайте программу
def get_password(n: int):
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    while True:
        yield ''.join([
            chars[random.randint(0, len(chars) - 1)] for _ in range(n)
        ])


gen = get_password(int(input()))
print(*[next(gen) for _ in range(5)], sep='\n')
