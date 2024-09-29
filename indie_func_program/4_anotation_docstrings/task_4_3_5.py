def rotate(lst: list[int | float], shift: int = 1) -> list[int | float]:
    """Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)"""
    new_list = lst[:]
    if shift < 0:
        new_list.reverse()
    for i in range(abs(shift)):
        el = new_list.pop()
        new_list.insert(0, el)
    if shift < 0:
        new_list.reverse()
    return new_list


def rotate_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    letters = list(range(97, 123))
    index = letters.index(ord(letter))
    letters = rotate(letters, -shift)
    return chr(letters[index])


def caesar_cipher(phrase: str, key: int) -> str:
    """Шифр Цезаря"""
    return ''.join(
        [rotate_letter(w, key) if w.isalpha() else w for w in phrase]
    )


print(caesar_cipher.__annotations__)
print(caesar_cipher.__doc__)
print(caesar_cipher('lost in the echo', 1))