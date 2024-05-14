with open('18_1_exam/temp.txt', encoding='utf-8') as f:
    file_data = list(f)
print(*file_data[-10:], sep='')