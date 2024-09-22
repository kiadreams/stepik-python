n = int(input())
count = 0
for i in range(n + 1, 2 * n):
    for d in range(2, i):
        if i % d == 0:
            break
    else:
        count += 1
print(count)