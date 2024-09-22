n = int(input())
s = 0
for i in range(n):
    row = list(map(int, input().split()))
    s += row[n]
print(s)

