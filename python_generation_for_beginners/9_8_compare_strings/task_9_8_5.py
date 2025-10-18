from string import digits

letters = 'абвгдежзийклмноп'
for _ in range(int(input())):
    cls = input().lower()
    answer = len(cls) == 2 and cls[0] in digits and cls[1] in letters
    print('YES' if answer else 'NO')
