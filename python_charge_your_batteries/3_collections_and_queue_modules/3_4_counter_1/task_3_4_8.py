from collections import Counter
from functools import reduce


def count_max_goals(stats: dict) -> Counter:
    return reduce(lambda r, x: r | Counter(x), stats.values(), Counter())
    result = Counter()
    for _, value in stats.items():
        result |= Counter(value)
    return result


statistics = {
    2020: {'Messi': 20, 'Neymar': 30, 'Ronaldo': 25},
    2021: {'Neymar': 23, 'Griezmann': 47, 'Messi': 29},
    2022: {'Griezmann': 35, 'Messi': 34, 'Ronaldo': 34}
}

assert count_max_goals(statistics) == Counter({'Griezmann': 47, 'Messi': 34, 'Ronaldo': 34, 'Neymar': 30})

statistics = {
    2015: {'Benzema': 32, 'Griezmann': 43, 'Messi': 52, 'Neymar': 39, 'Ronaldo': 51},
    2016: {'Benzema': 26, 'Griezmann': 37, 'Messi': 36, 'Neymar': 35, 'Ronaldo': 42},
    2017: {'Benzema': 27, 'Griezmann': 51, 'Messi': 42, 'Neymar': 49, 'Ronaldo': 30},
    2018: {'Benzema': 32, 'Griezmann': 41, 'Messi': 45, 'Neymar': 30, 'Ronaldo': 43},
    2019: {'Benzema': 29, 'Griezmann': 39, 'Messi': 51, 'Neymar': 31, 'Ronaldo': 48},
    2020: {'Benzema': 33, 'Griezmann': 41, 'Messi': 36, 'Neymar': 30, 'Ronaldo': 25},
    2021: {'Benzema': 54, 'Griezmann': 47, 'Messi': 29, 'Neymar': 36, 'Ronaldo': 21},
    2022: {'Benzema': 29, 'Griezmann': 35, 'Messi': 34, 'Neymar': 36, 'Ronaldo': 34}
}

assert count_max_goals(statistics) == Counter(
    {'Benzema': 54, 'Messi': 52, 'Griezmann': 51, 'Ronaldo': 51, 'Neymar': 49})
