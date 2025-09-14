from collections import Counter
from functools import reduce


def count_min_goals(stats: dict) -> Counter:
    # Вариант №1
    # players = {}
    # for year_data in stats.values():
    #     for name, goals in year_data.items():
    #         players.setdefault(name, []).append(goals)
    # return Counter({name: min(value) for name, value in players.items()})

    # Вариант №2
    all_stats = reduce(lambda x, y: x | y, map(Counter, stats.values()))
    new_stats = map(lambda d: Counter(all_stats | d), stats.values())
    return reduce(lambda x, y: x & y, new_stats)


statistics = {
    2020: {'Messi': 20, 'Neymar': 30, 'Ronaldo': 25},
    2021: {'Neymar': 23, 'Griezmann': 47, 'Messi': 29},
    2022: {'Griezmann': 35, 'Messi': 34, 'Ronaldo': 34}
}
assert count_min_goals(statistics) == Counter({'Griezmann': 35, 'Ronaldo': 25, 'Neymar': 23, 'Messi': 20})

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
assert count_min_goals(statistics) == Counter(
    {'Griezmann': 35, 'Neymar': 30, 'Messi': 29, 'Benzema': 26, 'Ronaldo': 21})