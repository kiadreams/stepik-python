from datetime import datetime
import pytz

dt_japan = datetime.now(pytz.timezone('Asia/Tokyo'))
print("Japan DateTime:", dt_japan.strftime("%Y:%m:%d %H:%M:%S %Z %z"))

dt_brazil = datetime.now(pytz.timezone('America/Sao_Paulo'))
print("Brazil DateTime:", dt_brazil.strftime("%Y:%m:%d %H:%M:%S %Z %z"))

dt_uk = datetime.now(pytz.timezone('Europe/London'))
print("Uk DateTime:", dt_uk.strftime("%Y:%m:%d %H:%M:%S %Z %z"))

dt_germany = datetime.now(pytz.timezone('Europe/Berlin'))
print("Germany DateTime:", dt_germany.strftime("%Y:%m:%d %H:%M:%S %Z %z"))

dt_aus = datetime.now(pytz.timezone('Australia/Canberra'))
print("Australia Oceanic DateTime:", dt_aus.strftime("%Y:%m:%d %H:%M:%S %Z %z"))

dt_africa = datetime.now(pytz.timezone('Africa/Maputo'))
print("Central Africa: DateTime:", dt_africa.strftime("%Y:%m:%d %H:%M:%S %Z %z"))
