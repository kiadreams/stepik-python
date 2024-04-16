st_1, st_2, st_3 = (set(map(int, input().split())) for _ in range(3))
answer = st_3.difference(st_1, st_2)
print(*sorted(answer, reverse=True))
