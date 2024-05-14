from random import choice, shuffle
from string import ascii_uppercase, ascii_lowercase, digits


s_up_case = list(set(ascii_uppercase).difference('IO'))
s_low_case = list(set(ascii_lowercase).difference('lo'))
s_dig = list(set(digits).difference('10'))
symbols = s_dig + s_up_case + s_low_case


def generate_password(length):
    password = [choice(i) for i in (s_up_case, s_low_case, s_dig)]
    password += [choice(symbols) for _ in range(3, length)]
    shuffle(password)
    return ''.join(password)


def generate_passwords(count, length):
    passwords = [generate_password(length) for _ in range(count)]
    return passwords


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')
