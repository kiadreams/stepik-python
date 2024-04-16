from datetime import datetime, date, timedelta

delta1 = datetime(2021, 1, 1, 12, 15, 20) - datetime(2020, 5, 1, 10, 5, 10)
delta2 = date(2020, 2, 29) - date(2019, 9, 1)
delta3 = date(2019, 9, 1) - date(2020, 2, 29)

print(delta1, '|', type(delta1))
print(delta2, '|', type(delta2))
print(delta3, '|', type(delta3))
print()
print(str(delta1), str(delta2), sep='\n')
print(repr(delta1), repr(delta2), sep='\n')

print()
delta = timedelta(days=-2, minutes=-300)
abs_delta = abs(delta)

print('Исходная:', delta.days, delta.seconds, delta, sep='\n')
print('С модулем:', abs_delta.days, abs_delta.seconds, abs_delta, sep='\n')

release = datetime(2022, 7, 15)
today = datetime(2022, 11, 6)

print(type(release - today))
