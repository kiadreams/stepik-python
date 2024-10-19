def my_range_gen(n, start=None, step=1):
    if step:
        n, start = (n, 0) if start is None else (start, n)
        while [start < n, start > n][step < 0]:
            yield start
            start += step


for i in my_range_gen(25, 4, -2):
    print(i)

print()

for i in my_range_gen(10, 30, 3):
    print(i)

print()

for i in my_range_gen(10, 30, 0):
    print(i)
