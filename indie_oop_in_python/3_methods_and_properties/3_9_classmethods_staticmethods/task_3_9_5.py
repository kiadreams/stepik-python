class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def from_str(str_format: str):
        day, month, year = map(int, str_format.split("-"))
        return Date(day, month, year)


# Проверка работы-------------------------------------------------------------
# Тест №1
day_1 = Date(20, 9, 1997)
assert day_1.day == 20
assert day_1.month == 9
assert day_1.year == 1997

# Тест №2
day_2 = Date.from_str('06-09-2022')
assert day_2.day == 6
assert day_2.month == 9
assert day_2.year == 2022
