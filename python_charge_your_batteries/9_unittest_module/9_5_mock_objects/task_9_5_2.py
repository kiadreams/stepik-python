import datetime
from unittest import mock

artyom_bd = datetime.date(1990, 8, 21)
with mock.patch('datetime.date', wraps=datetime.date) as datetime.date:
    print(datetime.date.today())  # Сегодняшняя дата
    datetime.date.today.return_value = artyom_bd
    print(datetime.date.today())  # ДР Артёма

print(datetime.date.today())  # Всё равно сегодняшняя дата
