phrase = [word.lower().strip(',.!?:;') for word in input().split()]
dict_word = {k: phrase.count(k) for k in set(phrase)}
answer = [word for word in dict_word
          if dict_word.get(word) == min(dict_word.values())]
print(sorted(answer)[0])
