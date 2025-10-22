from datetime import datetime


def is_available_date(booked_dates: list[str], date_for_booking: str):
    template = '%d.%m.%Y'
    start_date = end_date = date_for_booking
    if '-' in date_for_booking:
        start_date, end_date = date_for_booking.split('-')
    start_date = datetime.strptime(start_date, template).date()
    end_date = datetime.strptime(end_date, template).date()
    for dd in booked_dates:
        start = end = dd
        if '-' in dd:
            start, end = dd.split('-')
        start = datetime.strptime(start, template).date()
        end = datetime.strptime(end, template).date()
        if start_date > end or end_date < start:
            continue
        else:
            return False
    else:
        return True


if __name__ == '__main__':
    dates = ["04.11.2021", "05.11.2021-09.11.2021"]
    some_date = "01.11.2021"
    print(is_available_date(dates, some_date))

    dates = ['04.11.2021', '05.11.2021-09.11.2021']
    some_date = '01.11.2021-04.11.2021'
    print(is_available_date(dates, some_date))

    dates = ['04.11.2021', '05.11.2021-09.11.2021']
    some_date = '06.11.2021'
    print(is_available_date(dates, some_date))
