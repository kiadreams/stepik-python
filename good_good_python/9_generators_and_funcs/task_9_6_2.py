def get_sort(d):
    return [d[key] for key in sorted(d, reverse=True)]


d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}

print(get_sort(d))