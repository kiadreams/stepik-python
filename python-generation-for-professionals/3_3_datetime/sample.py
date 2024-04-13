from datetime import datetime, date, time

# Получение датавремени с помощью метода
# из текстового представления и его формата
some_dt = datetime.strptime('10/35/52', '%H/%M/%S')
print(some_dt)

print()
text = 'Experiment Date 01/28/2005; Time 23::50::13'
dt = datetime.strptime(text, 'Experiment Date %m/%d/%Y; Time %H::%M::%S')
print(dt)
