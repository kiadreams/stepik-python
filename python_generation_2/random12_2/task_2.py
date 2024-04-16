from random import sample
from string import ascii_uppercase as letters, digits


def generate_index():
    postal_code = [sample(letters, 2) + sample(digits, 2) for _ in range(2)]
    return ''.join(postal_code[0]) + '_' + ''.join(postal_code[1][::-1])
