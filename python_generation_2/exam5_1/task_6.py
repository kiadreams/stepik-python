def lines_are_correct(some_sequence) -> bool:
    return all(sorted(i) == sample for i in some_sequence)


n = int(input())
sample = list(range(1, n + 1))
matrix = [list(map(int, input().split())) for _ in range(n)]
result = lines_are_correct(matrix) and lines_are_correct(zip(*matrix))
print(('NO', 'YES')[result])
