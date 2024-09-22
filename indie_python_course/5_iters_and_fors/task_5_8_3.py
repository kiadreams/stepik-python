n = int(input())
team_colors = [list(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if team_colors[i][0] == team_colors[j][1]:
            count += 1
print(count)
