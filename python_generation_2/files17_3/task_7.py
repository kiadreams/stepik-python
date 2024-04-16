from random import choice


with (open('17_3_files/first_names.txt', encoding='utf-8') as f1,
      open('17_3_files/last_names.txt', encoding='utf-8') as f2):
    names, surnames = list(f1), list(f2)
for _ in range(3):
    print(f'{choice(names).rstrip()} {choice(surnames).rstrip()}')
