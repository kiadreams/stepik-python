import time


# Функция gmtime() принимает в качестве аргумента количество секунд, прошедших с начала эпохи, и возвращает кортеж struct_time в UTC.
# Если функции gmtime() передан аргумент None, то вернется значение time()
result = time.gmtime()
print('Результат:', result)
print('Год:', result.tm_year)
print('Месяц:', result.tm_mon)
print('День:', result.tm_mday)
print('Час:', result.tm_hour) # на 3 часа меньше, т.к. время по UTC.
print()
result = time.gmtime(None)
print('Результат:', result)
print('Год:', result[0])
print('Месяц:', result[1])
print('День:', result[2])
print('Час:', result[3])