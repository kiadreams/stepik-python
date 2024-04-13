n, answer = int(input()), []
x = n // 2
for i in range(n):
    temp = []
    for j in range(n):
        if i in (j, n - 1 - j, x) or j == x:
            temp.append('*')
        else:
            temp.append('.')
    print(' '.join(temp))
