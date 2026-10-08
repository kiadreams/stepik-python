words = {}
for w in input().split():
    if w in words:
        print(f"{w}_{words[w]}", end=' ')
    else:
        print(w, end=' ')
    words[w] = words.get(w, 0) + 1
