cities = (i for i in input().split())
for e in zip(cities, cities, cities):
    print(*e)
