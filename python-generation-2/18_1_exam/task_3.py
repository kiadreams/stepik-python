count = 0
with open('18_1_exam/grades.txt', encoding='utf-8') as f:
    for line in f:
        count += all(map(lambda x: int(x) >= 65, line.split()[1:]))
print(count)