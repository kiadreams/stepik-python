from datetime import datetime

patern = '%d.%m.%Y; %H:%M'
all_data, text = {}, []

with open('3_3_datetime/diary.txt', encoding='utf-8') as f:
    next_date = datetime.strptime(f.readline().strip(), patern)
    for line in f:
        string = line.strip()
        if string:
            text.append(string)
        else:
            all_data[next_date] = '\n'.join(text)
            text.clear()
            next_date = datetime.strptime(f.readline().strip(), patern)

all_data[next_date] = '\n'.join(text)
for key, value in sorted(all_data.items()):
    print(datetime.strftime(key, '%d.%m.%Y; %H:%M'))
    print(value)
    print()
