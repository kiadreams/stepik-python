from datetime import timedelta

delta_1 = timedelta(days=50)
delta_2 = timedelta(minutes=5, hours=28, weeks=2)
delta_3 = timedelta(hours=28, seconds=5, microseconds=10, milliseconds=39000)
delta_4 = timedelta(seconds=5)
delta_5 = timedelta(weeks=360, days=5, hours=6, minutes=2)

print(delta_1, type(delta_1))
print(delta_2, type(delta_2))
print(delta_3, type(delta_3))
print(delta_4, type(delta_4))
print(delta_5, type(delta_5))

"""
Экземпляр datetime.timedelta хранит все переданные данные только в виде
сочетания days, seconds и microseconds, а остальные переданные аргументы
инициализации конвертируются в эти единицы
"""