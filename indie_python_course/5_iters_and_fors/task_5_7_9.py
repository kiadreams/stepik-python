n, m = map(int, input().split())
max_sum, s = 0, 0
for i in range(n):
    row = [int(x) for x in input().split()]
    if (row_sum := sum(row)) > max_sum:
        max_sum, s = row_sum, i
print(max_sum, s, sep='\n')
