from collections import defaultdict

"""
Вам нужно создать словарь, который группирует сотрудников по отделам. Для этого
вы можете использовать defaultdict следующим образом:
"""
departs = [('Engineering', 'Alice Brown'),
           ('Engineering', 'Bob Smith'),
           ('Human Resources', 'Cindy Lee'),
           ('Marketing', 'David Johnson'),
           ('Marketing', 'Eva Martinez'),
           ('Sales', 'Frank Davis'),
           ('Sales', 'Gina Rodriguez')]

group_dep = defaultdict(list)
for department, employee in departs:
    group_dep[department].append(employee)

print(group_dep)

"""
Если пользоваться обычным словарем, код данной задачи мог выглядеть так:
"""

group_dep = dict()
for department, employee in departs:
    if department not in group_dep:
        group_dep[department] = [employee]
    else:
        group_dep[department].append(employee)
