n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
our_area = [elem for i, string in enumerate(matrix)
            for j, elem in enumerate(string)
            if i >= n - 1 - j]
print(max(our_area))