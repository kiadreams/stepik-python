import datetime
from unittest import mock

artyom_bd = datetime.date(1990, 8, 21)
curr_today = datetime.date.today
print(curr_today())
curr_today = mock.Mock(return_value=artyom_bd)
print(curr_today())
# with mock.patch('datetime.date', wraps=datetime.date) as datetime.date:
#     print(datetime.date.today())  # Сегодняшняя дата
#     datetime.date.today.return_value = artyom_bd
#     print(datetime.date.today())  # ДР Артёма
print(curr_today())
print(curr_today())
print(datetime.date.today())  # Всё равно сегодняшняя дата
