def print_cake(m):
    print()
    for el in m:
        print(el)
    print()


r, c = map(int, input().split())
pieces = 0
m = [input() for _ in range(r)]
for step in range(2):
    for i in range(c if step else r):
        if 'S' not in m[i]:
            pieces += m[i].count('.')
            m[i] = m[i].replace('.', '_')
    m = [''.join(el) for el in zip(*m)]
print(pieces)

