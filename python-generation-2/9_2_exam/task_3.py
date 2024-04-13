count = int(input())
cities = {input() for _ in range(count + 1)}
print(('OK', 'REPEAT')[len(cities) == count])
