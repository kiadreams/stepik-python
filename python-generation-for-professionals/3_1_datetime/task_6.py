from datetime import date


def get_date_range(start: date, end: date) -> list:
    result = []
    if start <= end:
        for i in range(start.toordinal(), end.toordinal() + 1):
            result.append(date.fromordinal(i))
    return result


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 2)

print(*get_date_range(date1, date2), sep='\n')
