with (open('17_4_files/class_scores.txt', encoding='utf-8') as inp_f,
      open('17_4_files/new_scores.txt', 'w', encoding='utf-8') as out_f):
    for line in inp_f:
        name, grade = line.split()
        new_grade = int(grade) + 5
        out_f.write(f'{name} {100 if new_grade > 100 else new_grade}\n')
