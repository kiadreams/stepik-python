values = [
    ("bb", 80),
    ("aa", 45),
    ("Bb", 5),
    ("ss", 43),
    ("AA", 80),
    ("BB", 8),
    ("Aa", 14),
]

print(sorted(values, key=lambda x: (x[0].lower(), int(x[1]))))
print()

values = [
    ("WW", 80),
    ("aa", 45),
    ("ee", 43),
    ("ss", 43),
    ("dd", 80),
    ("BB", 43),
    ("qqq", 14),
]
print(sorted(values, key=lambda x: (int(x[1]), x[0].lower()), reverse=True))
print()

sorted()