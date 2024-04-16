words, result = input().split(), set()
for word in words:
    result.add(word.strip(',.;:-!?').lower())
print(len(result))