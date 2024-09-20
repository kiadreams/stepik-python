number = list(int(n) for n in input())[::-1]
for i, n in enumerate(number, start=1):
    if not i % 2:
        number[i - 1] = n * 2 if n * 2 < 9 else n * 2 - 9
print(sum(number) % 10 == 0)