from audioop import reverse
from functools import wraps


def limit_query(n):
    def decorator(func):
        limit = 0

        @wraps(func)
        def inner(*args, **kwargs):
            nonlocal limit
            limit += 1
            if limit > n:
                print(f'Лимит вызовов закончен, все {n} попытки израсходованы')
                return None
            return func(*args, **kwargs)

        return inner

    return decorator

sum()
sorted()
max()
min()