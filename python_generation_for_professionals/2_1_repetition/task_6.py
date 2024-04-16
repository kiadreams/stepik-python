def filter_anagrams(word: str, words: list) -> list:
    return [w for w in words if sorted(w) == sorted(word)]


word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']
print(filter_anagrams(word, anagrams))

print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))

print(filter_anagrams('tommarvoloriddle',
                      ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))
print(filter_anagrams('стекло', []))

word = 'abba'
anagrams = ['aaab', 'dbcd', 'bdaa', 'badb']
print(filter_anagrams(word, anagrams))
