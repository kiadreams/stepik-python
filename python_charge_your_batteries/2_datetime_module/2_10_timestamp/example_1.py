from datetime import datetime
import sys


# Получаем текущую дату и время
dt = datetime.now()

# получаем timestamp
ts = dt.timestamp()

print("Time now is:", dt)
print("Timestamp is:", ts)
print()

sep_16_04 = datetime(2004, 9, 16)
print(sep_16_04)
print(sep_16_04.timestamp())
print()

oct_4_57 = datetime(1957, 10, 4)
print(oct_4_57)
# На windows выдает ошибку, так как windows не работает с timestamp...
if sys.platform != 'win32':
    print(oct_4_57.timestamp())
print()

print(datetime.now().timestamp())
