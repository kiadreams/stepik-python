n, m = map(int, input().split())
results = []
max_val = 0
for i in range(n):
    row = [int(x) for x in input().split()]
    if max_val < (val := max(row)):
        max_val = val
    results.append(row)
print(sum(1 for row in results if max_val in row))
