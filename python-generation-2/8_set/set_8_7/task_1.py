number_1, number_2 = input(), input()
result = set(number_1).isdisjoint(set(number_2))
print(('YES', 'NO')[result])
