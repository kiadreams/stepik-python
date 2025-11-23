from collections import defaultdict

subjects = [('Mathematics', 'Alice Brown'),
            ('Mathematics', 'Bob Smith'),
            ('Physics', 'Cindy Lee'),
            ('Chemistry', 'David Johnson'),
            ('Biology', 'Eva Martinez'),
            ('English', 'Frank Davis'),
            ('History', 'Gina Rodriguez'),
            ('Biology', 'Henry Wong'),
            ('Mathematics', 'Isabella Torres'),
            ('Physics', 'Jacob Hernandez'),
            ('Chemistry', 'Kevin Davis'),
            ('Biology', 'Liam Johnson'),
            ('English', 'Mia Anderson'),
            ('History', 'Noah Wilson'),
            ('Mathematics', 'Olivia Brown'),
            ('Physics', 'Paula Garcia'),
            ('Chemistry', 'Quincy Jones'),
            ('Biology', 'Robert Lee'),
            ('English', 'Sophia Davis'),
            ('History', 'Thomas Martinez'),
            ('Mathematics', 'Uma Patel'),
            ('Physics', 'Victor Brown'),
            ('Chemistry', 'William Johnson'),
            ('Biology', 'Xander Smith'),
            ('English', 'Yara Gonzalez'),
            ('History', 'Zoe Hernandez'),
            ('Mathematics', 'Aaron Davis'),
            ('Physics', 'Brian Wilson'),
            ('Chemistry', 'Catherine Brown'),
            ('Biology', 'Daniel Hernandez'),
            ('English', 'Emily Johnson'),
            ('History', 'Fiona Lee'),
            ('Mathematics', 'Gabriel Rodriguez'),
            ('Physics', 'Hannah Martinez'),
            ('Chemistry', 'Ian Smith')]

d = defaultdict(int)
for subject, _ in subjects:
    d[subject] += 1
d = sorted(list(d.items()), key=lambda x: (-x[1], x))
for subject, num in d:
    print(f'{subject}: {num}')
