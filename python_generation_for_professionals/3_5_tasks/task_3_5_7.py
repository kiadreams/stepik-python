from datetime import datetime, timedelta


pattern = '%d.%m.%Y'
cd = datetime.strptime(input(), pattern)
people = []

def chek_date(b_day: datetime):
    b_d, b_m = b_day.day, b_day.month
    for i in range(1, 8):
        curr_d = cd + timedelta(days=i)
        if curr_d.day == b_d and curr_d.month == b_m:
            return True
    else:
        return False

for _ in range(int(input())):
    name, d = input().rsplit(maxsplit=1)
    dt = datetime.strptime(d, pattern)
    if chek_date(dt):
        people.append((dt.date(), name))
print(sorted(people)[-1][-1] if people else 'Дни рождения не планируются')
