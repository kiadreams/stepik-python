def print_statistic(comments):
    c = {}
    for author, comment in sorted(comments, key=lambda x: x[0].lower()):
        c.setdefault(author, set()).add(comment)
    sort_c = {author: len(cmts) for author, cmts in sorted(c.items(), key=lambda x: -len(x[1]))}
    for author, cnt in sort_c.items():
        print(f'Количество уникальных комментаторов у {author} - {cnt}')


data = [
    ('karl', 'zhanna777'),
    ('karl', 'мама_игоречка_98'),
    ('qwerty03', 'pushka76'),
    ('Billy', 'мама_игоречка_98'),
    ('Billy', 'pushka76'),
    ('qwerty03', 'joebiden'),
    ('karl', 'zhanna777'),
    ('karl', 'joebiden'),
    ('karl', 'pushka76'),
]
print_statistic(data)