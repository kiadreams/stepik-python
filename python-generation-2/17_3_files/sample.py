with open('17_3_files/text_1.txt', encoding='utf-8') as f:
    print(f.read(), '\n')
    f.seek(0)               # Перемещаемся в начало документа
    f.readline()
    print(f.read(), '\n')
    f.seek(0)               # Перемещаемся в начало документа
    f.readline()
    mark_2 = f.tell()       # Получаем смещение начала второй строки
    f.readline()
    mark_3 = f.tell()       # Получаем смещение начала третьей строки
    print(mark_2, mark_3, f.read(), '', sep='\n')
    f.seek(mark_2)          # Перемещаемся в начало второй строки
    print(f.readline())     # И печатаем её
    f.seek(0)               # Перемещаемся в начало документа
    f.seek(mark_3)          # Перемещаемся в начало третьей строки
    print(f.readline())     # И печатаем её
    f.seek(mark_3)          # Снова перемещаемся в начало третьей строки!!!
    print(f.readline())     # И опять печатаем её!!!
    