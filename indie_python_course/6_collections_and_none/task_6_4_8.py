from string import ascii_lowercase
print(alphabet := dict([(w, i + 1) for i, w in enumerate(ascii_lowercase)]))
