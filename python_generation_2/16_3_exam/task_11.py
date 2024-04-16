ip_adds = [input() for _ in range(int(input()))]
func_map = lambda n: int(n[1]) * 256 ** (3 - n[0])
result = sorted(
    ip_adds,
    key=lambda x: sum(map(func_map, enumerate(x.split('.')))))
print(*result, sep='\n')