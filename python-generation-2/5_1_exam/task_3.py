n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = list(map(list, zip(*matrix)))
for elem in answer:
    print(*elem)