with (open('17_4_files/input.txt', encoding='utf-8') as input_f,
      open('17_4_files/output.txt', 'w', encoding='utf-8') as output_f):
    for i, line in enumerate(input_f, 1):
        output_f.write(f'{i}) {line}')