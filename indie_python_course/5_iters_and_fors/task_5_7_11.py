n, m = map(int, input().split())
results = []
for i in range(n):
    row = [int(x) for x in input().split()]
    result = max(row), sum(row), n - i
    results.append(result)
results.sort(reverse=True)
print(n - results[0][2])