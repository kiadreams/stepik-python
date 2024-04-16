with open('17_3_files/file.txt', encoding='utf-8') as f:
    data = list(f)
    num_strings = len(data)
    data = ' '.join(data)
    num_words = len(data.split())
    num_letters = sum(x.isalpha() for x in data)
    print(f'Input file contains:\n'
          f'{num_letters} letters\n'
          f'{num_words} words\n'
          f'{num_strings} lines')

