words = [len(set(input().lower())) for _ in range(int(input()))]
print(*words, sep='\n')