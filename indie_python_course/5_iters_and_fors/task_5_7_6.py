for i in range(5):
    row = [int(x) for x in input().split()]
    if any(row):
        j = row.index(1)
        print(abs(i - 2) + abs(j - 2))
        break
