from datetime import timedelta

delta1 = timedelta(seconds=57)
delta2 = timedelta(hours=25, seconds=2)

print(delta1 != 57)
print(delta2 == '5')

delta1 = timedelta(seconds=57)
delta2 = timedelta(hours=25, seconds=2)

print(delta2 > delta1)     # тут все ок
# print(delta2 > 5) # приводит к возникновению ошибки

