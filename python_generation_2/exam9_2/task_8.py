m, n = int(input()), int(input())
study_m = {input() for _ in range(m)}
study_n = {input() for _ in range(n)}
result = len(study_m ^ study_n)
answer = result if result else 'NO'
print(answer)