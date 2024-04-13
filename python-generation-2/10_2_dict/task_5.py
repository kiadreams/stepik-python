list_keys = ('CS101', 'CS102', 'CS103', 'NT110', 'CM241')
list_data = (['3004', 'Хайнс', '8:00'],
             ['4501', 'Альварадо', '9:00'],
             ['6755', 'Рич', '10:00'],
             ['1244', 'Берк', '11:00'],
             ['1411', 'Ли', '13:00'])
all_course, code = dict(zip(list_keys, list_data)), input()
if code in all_course:
    data = all_course[code]
    print(f'{code}: {data[0]}, {data[1]}, {data[2]}')
