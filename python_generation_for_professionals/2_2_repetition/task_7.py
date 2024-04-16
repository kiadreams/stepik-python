vowels = 'аеиоуюяёыэ'
sample = [i for i, v in enumerate(input()) if v in vowels]
for _ in range(int(input())):
    word = input()
    temp = [i for i, v in enumerate(word) if v in vowels]
    if sample == temp:
        print(word)
