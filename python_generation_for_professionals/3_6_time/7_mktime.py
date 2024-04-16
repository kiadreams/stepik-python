import time


# Функция mktime() принимает struct_time (или кортеж, содержащий 99 значений, относящихся к struct_time) в качестве аргумента и возвращает количество секунд, прошедших с начала эпохи, в местном времени.
time_tuple = (2021, 8, 31, 5, 31, 58, 1, 243, 0)
time_obj = time.mktime(time_tuple)
print('Локальное время в секундах:', time_obj)
print()
# !!! Функция mktime() является обратной к функции localtime(). Следующий пример показывает их связь:

seconds = 1630377118

time_obj = time.localtime(seconds)            # возвращает struct_time
print(time_obj)

time_seconds = time.mktime(time_obj)          # возвращает секунды из struct_time
print(time_seconds)