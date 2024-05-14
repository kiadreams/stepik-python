word = input()
dict_of_frequency = {word.count(symbol): symbol for symbol in set(word)}
for _ in range(int(input())):
    symbol, frequency = input().split(': ')
    word = word.replace(dict_of_frequency.get(int(frequency), ""), symbol)
print(word)

