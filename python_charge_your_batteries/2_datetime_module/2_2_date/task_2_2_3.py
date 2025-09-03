from datetime import date

dt = date(2023, 6, 7)

new_date = dt.replace(month=5, day=8)
print(new_date)