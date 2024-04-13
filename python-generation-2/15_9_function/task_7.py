is_excellent_student = [[True if input().split()[1] == '5' else False
                         for _ in range(int(input()))]
                         for _ in range(int(input()))]
print('YES' if all(any(stud) for stud in is_excellent_student) else 'NO')