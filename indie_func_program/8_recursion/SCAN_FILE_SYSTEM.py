import os


"""
Файловая система представляет собой иерархическую структуру с неопределенным
уровнем вложенности элементов: каталоги могут включать в себя файлы и другие
каталоги, которые в свою очередь тоже могут состоять из папок и файлов.
Идеальная ситуация для применения рекурсии.
"""
my_path = "e:/proba"


def scan_dir(path, level=1):
    print('Level=', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '//' + i):
            print('Спускаемся', path + '//' + i)
            scan_dir(path + '//' + i, level + 1)
            print('Возвращаемся в', path)


scan_dir(my_path)