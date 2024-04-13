# импортируем тип date из модуля datetime
from datetime import date, datetime

# создаем объект, соответсвующий дате урагана
hurricane_andrew = date(1992, 8, 24)

# выводим день недели
print(hurricane_andrew.weekday())

ts = 100000
some_date = datetime.fromtimestamp(ts)
print(some_date.date())