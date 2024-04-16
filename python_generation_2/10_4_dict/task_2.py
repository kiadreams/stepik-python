words = [input() for _ in range(2)]
dict_1 = {k: words[0].count(k) for k in set(words[0])}
dict_2 = {k: words[1].count(k) for k in set(words[1])}
print(result := 'YES' if dict_1 == dict_2 else 'NO')
