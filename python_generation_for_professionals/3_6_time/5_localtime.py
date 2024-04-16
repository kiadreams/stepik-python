import time


# Функция localtime() принимает в качестве аргумента количество секунд, прошедших с начала эпохи, и возвращает кортеж struct_time в локальном времени
# Если функции localtime() передан аргумент None, то вернется значение time()
curr_time = time.localtime()
print('Результат:', curr_time)
print('Год:', curr_time.tm_year)
print('Месяц:', curr_time.tm_mon)
print('День:', curr_time.tm_mday)
print('Час:', curr_time.tm_hour)
print()
curr_time = time.localtime(None)
print('Результат:', curr_time)
print('Год:', curr_time[0])
print('Месяц:', curr_time[1])
print('День:', curr_time[2])
print('Час:', curr_time[3])
