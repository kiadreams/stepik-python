m = input().split()[::-1]
x = int(input())
res = sum(map(lambda a, x: int(a[1]) * x ** a[0], enumerate(m), [x] * len(m)))
# result = map(lambda a, b: (a, b), enumerate(m), [x] * len(m))
print(res)
