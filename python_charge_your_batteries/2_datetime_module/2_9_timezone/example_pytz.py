from datetime import datetime
import pytz


"""
Использование pytz считается более надежным и удобным способом работы с
временными зонами и временем в Python. Этот модуль решает множество проблем,
связанных с управлением временными зонами, и позволяет избежать многих ошибок,
которые могут возникнуть при ручной обработке времени и временных зон без
использования специализированных библиотек.

Данный модуль является сторонним, поэтому его необходимо сперва установить.
С помощью pytz можно создавать информированные объекты datetime, которые
содержат информацию о временной зоне, что облегчает правильную работу со
временем и временными зонами. Для этого в модуле pytz имеется класс timezone,
в который необходимо передать правильно название того региона, локальное время
которого вы хотите увидеть
"""

# current Datetime
naive = datetime.now()
print('Timezone naive:', naive)

# Standard UTC timezone aware Datetime
aware = datetime.now(pytz.utc)
print('Timezone Aware:', aware)

# US/Central timezone datetime
aware_us_central = datetime.now(pytz.timezone('US/Central'))
print('US Central', aware_us_central)

# Moskow timezone datetime
aware_moskow = datetime.now(pytz.timezone('Europe/Moscow'))
print('Europe/Moscow', aware_moskow)
print(pytz.all_timezones_set)

