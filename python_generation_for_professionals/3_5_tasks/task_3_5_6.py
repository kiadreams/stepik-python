from datetime import datetime


pattern = '%d.%m.%Y'
people = {}
for _ in range(int(input())):
    dt = datetime.strptime(input().rsplit(maxsplit=1)[-1], pattern)
    people[dt] = people.get(dt, 0) + 1
max_dt = max(people.values())
count = sorted([d for d, _ in filter(lambda x: x[-1] == max_dt, people.items())])
print(*map(lambda x: x.strftime(pattern), count), sep='\n')
