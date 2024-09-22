froz = frozenset()
print(froz, type(froz))
print()

fr_abra = frozenset("abracadabra")
print(fr_abra)
print()

print([int("7" * i) for i in range(1, 78)])
print()

print(frozenset((1, 2, 2, 3, 3)) == frozenset((3, 2, 1, 1, 1)))
