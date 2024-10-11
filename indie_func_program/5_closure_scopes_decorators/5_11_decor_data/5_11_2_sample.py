d = {'a': 1, 'b': 2}
a = (3, 4)
c = (*a, *d.values())
m = d.items()
v = (*a, *m)
print(type(d.items()))
print({c: 1})
print({v: 1})

