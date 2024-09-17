n, m = map(int, input().split())
mat = []
for i in range(n):
    row = [int(x) for x in input().split()]
    mat.append(row)
print(*[sum(elem) for elem in mat])
mat = [x for x in zip(*mat)]
print(*[sum(elem) for elem in mat])