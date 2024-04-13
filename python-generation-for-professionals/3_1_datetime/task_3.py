from datetime import date


florida_hurricane_dates = [
    date(1951, 5, 23),
    date(1995, 6, 2),
    date(1954, 4, 12),
    date(2003, 8, 31),
    date(2010, 11, 13)
]


# счетчик для нужного количества ураганов
early_hurricanes = 0

# цикл по датам в которые был ураган
for hurricane in florida_hurricane_dates:
    # если месяц урагана меньше чем июнь (порядковый номер 6)
    if hurricane.month < 6:
        early_hurricanes += 1

print(early_hurricanes)
