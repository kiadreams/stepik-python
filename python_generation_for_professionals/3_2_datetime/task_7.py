from datetime import date


def print_good_dates(dates: list[date]):
    our_dates = filter(lambda x: x.year == 1992 and (x.month + x.day) == 29,
                       dates)
    for dt in sorted(our_dates):
        print(dt.strftime('%B %d, %Y'))


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)
print()
dates = [date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)]
print_good_dates(dates)
