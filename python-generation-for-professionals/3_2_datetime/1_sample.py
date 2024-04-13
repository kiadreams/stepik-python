from datetime import date, time
import locale
from pprint import pprint

my_date = date(2021, 8, 10)
my_time = time(7, 18, 34)


print(locale.getdefaultlocale())

print()
print(my_date.strftime(
    '%a %A %w %d %b %B %m %y %Y %H %I %p %M %S %f %z %Z %j %U %W %c %x %X'))
print(my_time.strftime(
    '%a %A %w %d %b %B %m %y %Y %H %I %p %M %S %f %z %Z %j %U %W %c %x %X'))
print()
# Использование локали для перевода имен к местному формату - Россия!!!
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
print(my_date.strftime(
    '%a %A %w %d %b %B %m %y %Y %H %I %p %M %S %f %z %Z %j %U %W %c %x %X'))
print(my_time.strftime(
    '%a %A %w %d %b %B %m %y %Y %H %I %p %M %S %f %z %Z %j %U %W %c %x %X'))
print()
# Использование локали для перевода имен к местному формату -
# возвращаем к поумолчанию!!!
locale.setlocale(locale.LC_ALL, locale.getdefaultlocale()[0])
print(my_date.strftime(
    '%a %A %w %d %b %B %m %y %Y %H %I %p %M %S %f %z %Z %j %U %W %c %x %X'))
print(my_time.strftime(
    '%a %A %w %d %b %B %m %y %Y %H %I %p %M %S %f %z %Z %j %U %W %c %x %X'))
print()
pprint(locale.locale_alias)
