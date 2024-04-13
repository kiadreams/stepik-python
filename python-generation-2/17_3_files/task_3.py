with open('17_3_files/lines.txt', encoding='utf-8') as file_i:
    data = list(map(str.strip, list(file_i)))
    result = filter(lambda x: len(x) == max(map(len, data)), data)
    print(*result, sep='\n')