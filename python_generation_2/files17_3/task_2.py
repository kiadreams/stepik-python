with open('17_3_files/data.txt', encoding='utf-8') as file_i:
    data = list(map(str.rstrip, list(file_i)))[::-1]
    print(*data, sep='\n')