from datetime import timezone, datetime, timedelta


"""
Наивный (Naive) объект не имеет информации о временной зоне и не учитывает
переходы на летнее и зимнее время.

Информированный (Aware) объект, напротив, содержит информацию о временной зоне
и учитывает переходы на летнее/зимнее время.
"""

# naive
naive = datetime.now()
print("Naive:", naive)


# Создание datetime в московском часовом поясе MSK
msk_dateTime = datetime.now(timezone(timedelta(hours=+3)))
print("Aware - In MSK:", msk_dateTime)
after_hour = timedelta(hours=1)
print("Aware after 1 hour - In MSK:", msk_dateTime + after_hour)
