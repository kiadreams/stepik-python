def data_file(name_file):
    with open('17_4_files/' + name_file, encoding='utf-8') as f:
        return f.read()


file_list = [input() for _ in range(int(input()))]
with open('17_4_files/output.txt', 'w', encoding='utf-8') as out_f:
    for name_file in file_list:
        out_f.write(data_file(name_file))
