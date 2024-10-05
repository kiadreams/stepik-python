def print_best_and_worst_laureate(laurs):
    l = sorted(laurs.values(), key=lambda x: list(laurs.values()).count(x))
    print(f'{l[-1]}, {l.count(l[-1])}\n{l[0]}, {l.count(l[0])}')


laureates = {'За лучший фильм': 'Оппенгеймер',
             'За лучшую музыку к фильму': 'Оппенгеймер',
             'За лучший звук': 'Зона интересов',
             'За лучшие визуальные эффекты': 'Бедные-несчастные',
             'За лучший дизайн костюмов': 'Бедные-несчастные',
             'За лучшую операторскую работу': 'Бедные-несчастные',
             'За лучший монтаж': 'Оппенгеймер',
             'За лучший оригинальный сценарий': 'Оппенгеймер',
             'За лучший фильм на иностранном языке': 'Зона интересов'}

print_best_and_worst_laureate(laureates)