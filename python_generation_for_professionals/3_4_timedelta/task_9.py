from datetime import timedelta, datetime


def fill_up_missing_dates(dates: list[str]) -> list:
    format = '%d.%m.%Y'
    dts = [datetime.strptime(dt, format).date() for dt in dates]
    min_d, max_d = min(dts), max(dts),
    days = (max_d - min_d).days
    return [(min_d + timedelta(days=n)).strftime(format)
            for n in range(days + 1)]
    # return result
    dts.sort()
    # result = []
    print(dts)
    result = dts[:1]
    print(result)
    for i in range(1, len(dts)):
        days = abs((result[-1] - dts[i]).days)
        for _ in range(days):
            result.append(result[-1]+timedelta(days=1))
            print(result)
    return result


# dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']
print(fill_up_missing_dates(dates))