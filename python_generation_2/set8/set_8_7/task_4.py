st_1, st_2, st_3 = (set(map(int, input().split())) for _ in range(3))
grades_in_three = st_1 & st_2 & st_3
answer = st_1.union(st_2, st_3).difference(grades_in_three)
print(*sorted(answer))
