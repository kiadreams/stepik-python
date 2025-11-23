from collections import Counter
from string import punctuation, whitespace


text = input().lower()
counter = Counter(x for x in text if x not in (punctuation + whitespace))
for key, value in counter.items():
    print(key, value)
