n = int(input())
m = [[int(x) for x in input().split()] for _ in range(n)]
print("Yes" if m == [list(el) for el in zip(*m)] else "No")