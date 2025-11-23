from datetime import datetime, timezone, timedelta


# Создаем объект datetime в UTC
utc_datetime = datetime.now(timezone.utc)

# Создаем объект временной зоны для желаемого часового пояса (например, New York)
ny_timezone = timezone(timedelta(hours=-4))  # UTC-4 для Eastern Time Zone (ET)

# Преобразуем объект datetime из UTC в New York Time
ny_datetime = utc_datetime.astimezone(ny_timezone)

print("Время в UTC:", utc_datetime)
print("Время в New York Time:", ny_datetime)