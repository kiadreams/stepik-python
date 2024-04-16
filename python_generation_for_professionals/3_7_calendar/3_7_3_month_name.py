import calendar, locale


english_names = list(calendar.month_name)
print(english_names)

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

russian_names = list(calendar.month_name)
print(russian_names)