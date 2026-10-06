import string

words = {}
translate_table = str.maketrans('', '', string.punctuation)
text = input().lower().translate(translate_table)
list_of_words = text.split()
for word in list_of_words:
    words[word] = words.get(word, 0) + 1
min_count = min(words.values())
f_words = filter(lambda x: words[x] == min_count, words)
print(min(list(f_words)))
