DICTIONARY = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cat',
    'd': 'dog',
}


def alphabet():
    letter = yield
    while True:
        try:
            letter = yield DICTIONARY.get(letter, 'default')
        except KeyError:
            letter = 'default'


coro = alphabet()
next(coro)
print(coro.send('a'))
print(coro.send('b'))
print(coro.throw(KeyError))
print(coro.send('c'))

print()

coro = alphabet()
next(coro)
print(coro.send('apple'))
print(coro.send('banana'))
print(coro.throw(KeyError))
print(coro.send('dog'))
print(coro.send('d'))

print()

coro = alphabet()
next(coro)
print(coro.send('a'))
print(coro.send('b'))
print(coro.throw(KeyError))
print(coro.send('c'))

