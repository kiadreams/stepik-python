def get_info_marks(students, *marks):
    grades = [{'best': max(i), 'worst': min(i)} for i in list(zip(*marks))]
    return dict(zip(students, grades))


math = [90, 76, 94]
history = [78, 79, 90]
geography = [95, 80, 92]
music = [93, 98, 100]
students = ["Marie", "Michael", "Marge"]
print(get_info_marks(students, math, geography, history, music))