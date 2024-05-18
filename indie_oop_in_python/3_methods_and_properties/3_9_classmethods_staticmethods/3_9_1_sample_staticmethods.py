class LengthConverter:
    METER = "m"
    KILOMETER = "km"
    MILE = "mi"

    @staticmethod
    def meters_to_kilometers(m):
        return m / 1000

    @staticmethod
    def kilometers_to_meters(km):
        return km * 1000

    @staticmethod
    def meters_to_miles(m):
        return m / 1609.34

    @staticmethod
    def miles_to_meters(mi):
        return mi * 1609.34

    @staticmethod
    def kilometers_to_miles(km):
        return km / 1.60934

    @staticmethod
    def miles_to_kilometers(mi):
        return mi * 1.60934

    @staticmethod
    def format(value, unit):
        symbol = ""
        if unit == LengthConverter.METER:
            symbol = "m"
        elif unit == LengthConverter.KILOMETER:
            symbol = "km"
        elif unit == LengthConverter.MILE:
            symbol = "mi"

        return f"{value}{symbol}"


some_convert = LengthConverter()
print(some_convert.meters_to_miles(560))
