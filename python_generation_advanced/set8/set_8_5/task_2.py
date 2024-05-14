words = [input().lower() for _ in range(int(input()))]
result = set(''.join(words))
print(len(result))