m, n = int(input()), int(input())
study_m = {input() for _ in range(m)}
study_n = {input() for _ in range(n)}
print(len(study_m - study_n))
