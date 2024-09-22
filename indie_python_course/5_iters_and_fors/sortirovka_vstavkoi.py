n = int(input())
lst = [int(x) for x in input().split()]
for i in range(1, n):
    for j in range(i, 0, -1):
        if lst[j] < lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
print(*lst)