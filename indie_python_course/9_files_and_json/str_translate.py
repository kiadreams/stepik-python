a = {'a': '1', 'b': '4'}
s = 'adsbaabb!'
tabl = s.maketrans(a)
print(tabl)
print(s.translate(tabl))
print(s.translate(tabl))