from datetime import datetime

date_string = "02.09.2023"
time_string = "10:20:18"

dt = datetime.strptime(date_string, "%d.%m.%Y")  # В dt будет datetime
print(dt, type(dt))  # 2023-09-02 00:00:00 <class 'datetime.datetime'>
date_obj = dt.date()  # преоразуем в date
print("Объект date:", date_obj)  # Объект date: 2023-09-02
print(type(date_obj))  # <class 'datetime.date'>

# Либо можно сразу в одной строке сделать преобразование

date_obj_2 = datetime.strptime(date_string, "%d.%m.%Y").date()

print("Объект date 2:", date_obj_2)  # Объект date 2: 2023-09-02
print(type(date_obj_2))  # <class 'datetime.date'>

dt_from_time = datetime.strptime(time_string, '%H:%M:%S')
print(dt_from_time)
