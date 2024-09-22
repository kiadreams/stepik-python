def my_range_gen(stop, start=0, step=1):
    if start:
        start, stop = stop, start
    while step != 0 and (start < stop if step > 0 else start > stop):
        yield start
        start += step


# Ничего не печатает
for i in my_range_gen(4, 8, 0):
    print(i)
for i in my_range_gen(20, 10, 3):
    print(i)
# Ничего не печатает, потому что нельзя пройти от 20 до 10 с шагом 3
for i in my_range_gen(1, 10, -2):
    print(i)
# Ничего не печатает, потому что нельзя пройти от 1 до 10 с шагом -2

for i in my_range_gen(4, 8, 2):
    print(i)
print()
# Будет напечатано
# 4
# 6
for i in my_range_gen(8, 5, -1):
    print(i)
print()
# Будет напечатано
# 8
# 7
# 6
for i in my_range_gen(4, 8):
    print(i)
print()
# Будет напечатано
# 4
# 5
# 6
# 7
for i in my_range_gen(5):
    print(i)
print()
# Будет напечатано
# 0
# 1
# 2
# 3
# 4