from string import punctuation

def longest_word_in_file(file_name: str) -> str:
    words = {}
    with open(file_name, encoding='utf=8') as fi:
        for line in fi:
            new_line = ''.join(w for w in line if w not in punctuation)
            for word in new_line.split():
                words[len(word)] = word
    return words[max(words)]

print(longest_word_in_file('1.txt'))