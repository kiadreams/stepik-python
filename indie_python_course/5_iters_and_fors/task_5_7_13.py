is_cool = True
m = [input() for _ in range(4)]

for i in range(3):
    for j in range(3):
        if m[i][j] == m[i][j + 1] == m[i + 1][j] == m[i + 1][j + 1]:
            is_cool = False
            break
    if not is_cool:
        break
print("Yes" if is_cool else "No")
