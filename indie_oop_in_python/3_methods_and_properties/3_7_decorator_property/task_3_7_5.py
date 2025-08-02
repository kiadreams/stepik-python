class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        self.name = name
        self.offset_hours = offset_hours
        self.offset_minutes = offset_minutes

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, time_zone_name):
        if isinstance(time_zone_name, str) and time_zone_name.strip():
            self.__name = time_zone_name.strip()
        else:
            raise ValueError(f'Timezone bad name - {time_zone_name}')

    @property
    def offset_hours(self):
        return self.__offset_hours

    @offset_hours.setter
    def offset_hours(self, hours):
        if not isinstance(hours, int):
            raise ValueError("Hour offset must be an integer.")
        elif -13 < hours < 15:
            self.__offset_hours = hours
        else:
            raise ValueError('Offset must be between -12:00 and +14:00.')

    @property
    def offset_minutes(self):
        return self.__offset_minutes

    @offset_minutes.setter
    def offset_minutes(self, minutes):
        if not isinstance(minutes, int):
            raise ValueError("Minutes offset must be an integer.")
        elif -60 < minutes < 60:
            self.__offset_minutes = minutes
        else:
            raise ValueError("Minutes offset must between -59 and 59.")


# ------------------------------------------------------------------------
# тест №1

tz1 = TimeZone('ABC', -2, -15)
assert tz1.name == 'ABC'
assert tz1.offset_hours == -2
assert tz1.offset_minutes == -15

tz1.name = "XYZ"
tz1.offset_hours = 12
tz1.offset_minutes = 0


try:
    tz1.offset_hours = 67
except ValueError as e:
    assert e.__str__() == 'Offset must be between -12:00 and +14:00.'
assert tz1.name == 'XYZ'
assert tz1.offset_hours == 12
assert tz1.offset_minutes == 0

# --------------------------------------------------------------------------
# тест №2

for name in ['', None, '    ', 123, (1, 3), True]:
    try:
        TimeZone(name, 5, 34)
    except ValueError as e:
        assert e.__str__() == f'Timezone bad name - {name}'