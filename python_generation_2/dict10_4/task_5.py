n, countries = int(input()), {}
for _ in range(n):
    country, *cities = input().split()
    countries.update(dict.fromkeys(cities, country))
for _ in range(int(input())):
    print(countries[input()])
