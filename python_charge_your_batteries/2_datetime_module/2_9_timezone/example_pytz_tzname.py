from datetime import datetime
import pytz

# timezone: US Central Time
dt_us_central = datetime.now(pytz.timezone('America/Mexico_City'))
print("US Central DateTime:", dt_us_central.strftime("%Y:%m:%d %H:%M:%S %Z %z"))

# Получение названия временной зоны
print(dt_us_central.tzname())

# Получить смещение относительго UTC
print(dt_us_central.utcoffset())

# Получить смещение по летнему времени
print(dt_us_central.dst())
