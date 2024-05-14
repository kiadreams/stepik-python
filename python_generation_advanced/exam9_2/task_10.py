m, n = int(input()), int(input())
students = [input() for _ in range(m + n)]
result = len(set(students)) * 2 - (n + m)
print(result if result else 'NO')

