all_files, measures = {}, {'GB': 1024**3, 'MB': 1024**2, 'KB': 1024, 'B': 1}

def get_measure(size: int) -> tuple:
    """Определяет размерность и округленное значение размера файлов"""
    rounded_size, cur_measure = 0, 'B' 
    for measure in measures:
        rounded_size = round(size / measures[measure])
        if rounded_size >= 1:
            cur_measure = measure
            break
    return rounded_size, cur_measure

# Читаем имена файлов в словарь:
# расширение - ключ; имя файла и размер в байтах - значение
with open('2_2_repetition/files.txt', encoding='utf-8') as f:
    for line in f.readlines():
        name, size, measure = line.split()
        extension = name.split('.')[1]
        file = (name, int(size) * measures[measure])
        all_files.setdefault(extension, []).append(file)

# В цикле для каждого расширения выводим файлы, общий их размер и размерность 
for exten, files in sorted(all_files.items()):
    size_files = sum([file[1] for file in files])
    file_names = [file[0] for file in files]
    rounded_size, measure = get_measure(size_files)
    print(*sorted(file_names), sep='\n')
    print('----------')
    print(f'Summary: {rounded_size} {measure}\n')
