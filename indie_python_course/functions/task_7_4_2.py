def get_word_indices(strings: list[str]) -> dict:
    dict_words = {}
    for i, line in enumerate(strings):
        for word in line.lower().split():
            dict_words.setdefault(word, []).append(i)
    return dict_words


get_word_indices(["This is a string", "test String", "test", "string"])
