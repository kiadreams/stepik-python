import json

# Первый вариант...
with open("Alphabet.json", encoding="utf-8") as f_json:
    d = json.load(f_json)
with open("Abracadabra__1_.txt", encoding="utf-8") as f_text:
    text1 = "".join(d.get(w, w) for w in f_text.read())
print(text1)
print()

# Второй вариант
with open("Alphabet.json", encoding="utf-8") as f_json:
    data_dct = json.load(f_json)
with open("Abracadabra__1_.txt", encoding="utf-8") as f_text:
    text2 = f_text.read()
table_tr = text2.maketrans(data_dct)
t_text = text2.translate(table_tr)
print(t_text)
