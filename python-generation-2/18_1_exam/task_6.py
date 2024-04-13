def get_forbidden_words():
    with open('18_1_exam/forbidden_words.txt', encoding='utf-8') as f:
        file_data = f.read().strip().split()
    return {word: '*' * len(word) for word in file_data}


with open('18_1_exam/temp.txt', encoding='utf-8') as f:
    data = f.read()
    data_lowcase = data.lower()
    for word, value in get_forbidden_words().items():
        data_lowcase = data_lowcase.replace(word, value)
    text = ''.join(y if y == '*' else x for x, y in zip(data, data_lowcase))
    print(text)
