n, m = map(int, input().split())
max_val = (0, 0, 0)
for i in range(n):
    row = [int(x) for x in input().split()]
    if max_val[0] < (val := max(row)):
        max_val = (val, i, row.index(val),)
print(f"{max_val[0]}\n{max_val[1]} {max_val[2]}")