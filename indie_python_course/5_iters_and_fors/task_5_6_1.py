count = 0
for i1 in range (1, 10):
    for i2 in range(10):
        for i3 in range(10):
            for i4 in range(10):
                if i1 + i2 + i3 + i4 == 20:
                    count += int(f"{i1}{i2}{i3}{i4}")
print(count)