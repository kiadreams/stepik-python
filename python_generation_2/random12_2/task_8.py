from random import choice
from string import ascii_letters, digits


def generate_password(length):
    symbols = list(set(ascii_letters + digits).difference('lI1oO0'))
    password = ''.join([choice(symbols) for _ in range(length)])
    return password


def generate_passwords(count, length):
    passwords = [generate_password(length) for _ in range(count)]
    return passwords


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')
