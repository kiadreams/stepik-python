def is_leap(year):
    return (year % 100 != 0 or year % 400 == 0) and year % 4 == 0

def count_leap_years(y1, y2):
    count_leap = 0
    for y in range(y1, y2):
        if is_leap(y):
            count_leap += 1
    return count_leap


print(count_leap_years(2000, 2018))

print(sorted('asdfffdsa'))

print()

print(max(['sdf', 'sdf', 'safag'], key=len))

print('raspocovka'.center(30, '-'))
*values, = [1, 2, 3, 4, 5]
print(values)