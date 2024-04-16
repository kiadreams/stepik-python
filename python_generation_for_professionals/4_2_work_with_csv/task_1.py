import csv

with open('4_2_work_with_csv/grades.csv', encoding='utf-8') as csv_file:
    # считываем содержимое файла
    text = csv.reader(csv_file, delimiter=';')
    # создаем reader объект и указываем в качестве разделителя символ ;
    # rows = csv.reader(text, delimiter=';')
    # выводим каждую строку
    for row in text:
        print(row)
