st_1, st_2, st_3 = (set(map(int, input().split())) for _ in range(3))
result = sorted(st_1.intersection(st_2).difference(st_3), reverse=True)
print(*result)
