import calendar, locale

for name in calendar.day_name:
    print(name)
print()

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

for name in calendar.day_name:
    print(name)
print()

names = list(calendar.day_name)
print(names)