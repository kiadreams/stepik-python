import time


# Функция asctime() принимает struct_time (или кортеж, содержащий 99 значений, относящихся к struct_time) в качестве аргумента и возвращает строку, представляющую собой дату и время.
time_tuple = (2021, 8, 31, 5, 31, 58, 1, 243, 0)

result = time.asctime(time_tuple)
print('Результат:', result)
print()

# Функции ctime() и asctime() имеют практически одинаковый функционал, за тем исключением, что первая функция принимает количество прошедших от начала эпохи секунд, а вторая принимает struct_time (или соответствующий кортеж). Обе функции представляют время в более удобном виде, благодаря автоматическому форматированию.
seconds = 1530377118
time_tuple = (2021, 8, 31, 5, 31, 58, 1, 243, 0)

print(time.ctime(seconds))
print(time.asctime(time_tuple))