from datetime import datetime, timezone


"""
У класса timezone не так много атрибутов: min, max и utc
Атрибуты min и max показывают минимальное и максимальное возможные смещения
"""
print("Min", timezone.min)
print("Max", timezone.max)
print()

"""
Атрибут utc позволяет создать информированный объект по времени UTC
"""
print("UTC", timezone.utc)

UTC = datetime.now(timezone.utc)
print("UTC datetime", UTC)

