from collections import Counter
from functools import reduce


def calculate_sales(*sales_dicts) -> Counter:
    return reduce(lambda s, x: s + Counter(x), sales_dicts, Counter())


# Пример использования функции
sales_1 = {'John': 10, 'Mary': 5, 'Bob': 3, 'Alice': 7}
sales_2 = {'John': 5, 'Mary': 8, 'Bob': 6, 'Alice': 2}
sales_3 = {'John': 3, 'Mary': 4, 'Bob': 2, 'Alice': 9}
sales_4 = {'John': 8, 'Alice': 5, 'Henry': 10}

assert calculate_sales(sales_1, sales_2, sales_3) == Counter({'John': 18, 'Alice': 18, 'Mary': 17, 'Bob': 11})
assert calculate_sales(sales_1, sales_2) == Counter({'John': 15, 'Mary': 13, 'Bob': 9, 'Alice': 9})
assert calculate_sales(sales_3, sales_2) == Counter({'Mary': 12, 'Alice': 11, 'John': 8, 'Bob': 8})
assert calculate_sales(sales_4, sales_2, sales_1) == Counter({'John': 23, 'Alice': 14, 'Mary': 13, 'Henry': 10, 'Bob': 9})
