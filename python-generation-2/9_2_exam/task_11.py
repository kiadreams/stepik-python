result = set()
for _ in range(int(input())):
    if not result:
        result.update(input() for _ in range(int(input())))
    else:
        result.intersection_update(input() for _ in range(int(input())))
print(*sorted(result), sep='\n')
