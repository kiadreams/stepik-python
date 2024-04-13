st_1, st_2, st_3 = (set(map(int, input().split())) for _ in range(3))
answer = set(range(11)).difference(st_1, st_2,st_3)
print(*sorted(answer))