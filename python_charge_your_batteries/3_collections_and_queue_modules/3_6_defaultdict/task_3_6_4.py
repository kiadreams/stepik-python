from collections import defaultdict


magic = 'abracadabraabracadabraabracadabra'
statistics = defaultdict(list)
for index, letter in enumerate(magic):
    statistics[letter].append(index)
print(statistics)