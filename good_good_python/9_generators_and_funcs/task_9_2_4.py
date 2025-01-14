import random
from string import ascii_lowercase, ascii_uppercase
from typing import Generator


random.seed(1)


def get_email(max_size: int) -> Generator[str, None, None]:
    chars = ascii_lowercase + ascii_uppercase
    while True:
        lg = [
            chars[random.randint(0, len(chars) - 1)] for _ in range(max_size)
        ]
        yield ''.join(lg) + '@mail.ru'


gen = get_email(int(input()))
print(*[next(gen) for _ in range(5)], sep='\n')
