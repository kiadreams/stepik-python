with open('18_1_exam/words.txt', encoding='utf-8') as f:
    file_data = f.read().split()
max_len = len(max(file_data, key=len))
result = filter(lambda x: len(x) == max_len, file_data)
print(*result, sep='\n')