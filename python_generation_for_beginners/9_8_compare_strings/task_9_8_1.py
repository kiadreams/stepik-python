strs = sorted([input() for _ in range(4)], key=lambda x: len(x))
print((ord(min(strs)[-1]) * ord(max(strs)[-1])) ** 2)
