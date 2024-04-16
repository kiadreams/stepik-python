word_1, word_2, word_3 = input().split()
result = ('NO', 'YES')[set(word_1) == set(word_2) == set(word_3)]
print(result)