from math import factorial as fact

cache = {}


def factorial(value: int) -> int:
    """Вычисляем, кешируем и возвращаем значение факториала"""
    if value in cache:
        print(f"Get from cache value factorial({value})")
    return cache.setdefault(value, fact(value))


print(cache)
print(factorial(3))
print(cache)
print(factorial(5))
print(cache)
print(factorial(3))

print(dir(__builtins__), len(dir(__builtins__)))

