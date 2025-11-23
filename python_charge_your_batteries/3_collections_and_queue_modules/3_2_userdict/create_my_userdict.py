from collections import UserDict


class FrequencyDict(UserDict):
    def add_word(self, word):
        self.data[word] = self.data.get(word, 0) + 1


freq_dict = FrequencyDict()
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
for word in words:
    freq_dict.add_word(word)

print(freq_dict)
print('-' * 30)


class CaseInsensitiveDict(UserDict):
    def __getitem__(self, key):
        # Преобразование ключа к нижнему регистру
        key_lower = key.lower()
        # Возвращение значения по преобразованному ключу
        return self.data[key_lower]

    def __setitem__(self, key, value):
        # Преобразование ключа к нижнему регистру
        key_lower = key.lower()
        # Сохранение значения по преобразованному ключу
        super().__setitem__(key_lower, value)

    def keys(self):
        raise NotImplemented("Not allowed")


d = CaseInsensitiveDict()
d["KeY"] = "Secret"
d["HELLO"] = 123
print(d)
print(d["keY"])
