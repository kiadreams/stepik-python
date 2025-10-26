from datetime import datetime
from collections import defaultdict


pattern = '%d.%m.%Y'
people = [input().rsplit(maxsplit=1) for _ in range(int(input()))]
age_of_people = defaultdict(list)
for date in people:
    name, d = date
    age_of_people[datetime.strptime(d, pattern)].append(name)
old_dt = min(age_of_people)
old_people = age_of_people[old_dt]
print(old_dt.strftime(pattern), old_people[0] if len(age_of_people[old_dt]) == 1 else len(old_people))
