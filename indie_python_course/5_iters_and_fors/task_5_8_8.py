a, b = map(int, input().split())
is_color = False
m = []
for _ in range(a):
    row = input()
    if 'M' in row or 'Y' in row or 'C' in row:
        is_color = True
print('#Color' if is_color else '#Black&White')