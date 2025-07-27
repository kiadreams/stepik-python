from datetime import date


curr_dt = date(2014, 1, 1)
end_dt = date(2022, 12, 31)
result = []


def add_one_day(dt: date) -> date:
    try:
        new_date = dt.replace(day=dt.day + 1)
    except ValueError as e:
        try:
            new_date = dt.replace(month=dt.month + 1, day=1)
        except ValueError as e:
            new_date = dt.replace(year=dt.year + 1, month=1, day=1)
    return new_date


while curr_dt != end_dt:
    curr_dt = add_one_day(curr_dt)
    if curr_dt.isoweekday() == 1 and curr_dt.day == 1:
        result.append(curr_dt)
print(len(result))
