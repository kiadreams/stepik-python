DICTIONARY = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cat',
    'd': 'dog',
}


def alphabet():
    letter = None
    while True:
        letter = yield DICTIONARY.get(letter)


coro = alphabet()
next(coro)
print(coro.send('a'))
print(coro.send('b'))
print(coro.send('c'))