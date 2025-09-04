from datetime import date, datetime, time

iso_date_str = "2023-09-02"

# Преобразование iso-строки в объект date
date_obj = date.fromisoformat(iso_date_str)

print("Объект date:", date_obj)  # Объект date: 2023-09-02
print(type(date_obj))  # <class 'datetime.date'>
print()

iso_datetime_str = "2023-09-02T15:30:00"

# Преобразование iso-строки в объект datetime
datetime_obj = datetime.fromisoformat(iso_datetime_str)

print("Объект datetime:", datetime_obj)  # Объект datetime: 2023-09-02 15:30:00
print(type(datetime_obj))  # <class 'datetime.datetime'>
print()

iso_time_str = "15:30:00"

# Преобразование iso-строки в объект time
time_obj = time.fromisoformat(iso_time_str)

print("Объект time:", time_obj)  # Объект time: 15:30:00
print(type(time_obj))  # <class 'datetime.time'>