n, answers = int(input()), {}
for _ in range(n):
    word, synonym = input().split()
    answers[word], answers[synonym] = synonym, word
print(answers[input()])
