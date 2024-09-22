pair = {"B": "W", "W": "B"}
n, m = map(int, input().split())
photo = [input() for _ in range(n)]
input()
negative = [input() for _ in range(n)]
pixel = 0
for i in range(n):
    for j in range(m):
        if pair.get(photo[i][j]) != negative[i][j]:
            pixel += 1
print(pixel)
