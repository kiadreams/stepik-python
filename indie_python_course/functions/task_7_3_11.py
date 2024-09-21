def count_AGTC(dna):
    agtc = {"A": 0, "G": 0, "T": 0, "C": 0}
    for e in dna:
        agtc[e] += 1
    return tuple(agtc.values())


# код ниже не стоит удалять, он нужен для проверки
assert count_AGTC("AGGTC") == (1, 2, 1, 1)
assert count_AGTC("AAAATTT") == (4, 0, 3, 0)
assert count_AGTC("AGTTTTT") == (1, 1, 5, 0)
assert count_AGTC("CCT") == (0, 0, 1, 2)
print("Проверки пройдены")