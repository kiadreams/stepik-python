from collections import defaultdict


def get_inventory() -> set:
    return {'меч', 'лук', 'щит', 'зелье'}


heroes = defaultdict(get_inventory)
for _ in range(int(input())):
    name, subject = input().split()
    heroes[name] -= {subject} if subject in heroes[name] else heroes[name]
for name in ('Артур', 'Борис', 'Виктор'):
    subjects = heroes[name]
    if subjects:
        print(f'{name}: {", ".join(sorted(subjects))}')

