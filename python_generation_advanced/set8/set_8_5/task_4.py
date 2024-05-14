numbers, set_numbers = list(map(int, input().split())), set()
for number in numbers:
    if number in set_numbers:
        print('YES')
    else:
        print('NO')
    set_numbers.add(number)
