month = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday',
         'Thursday', 'Friday']
days = ((d, wd) for wd, d in zip(month * 11, range(1, 78)))
for day in days:
    print(day)