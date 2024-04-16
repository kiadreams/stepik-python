# price = {1: 'AEILNORSTU', 2: 'DG', 3: 'BCMP',
#          4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# result = [key for i in input() for key in price if i in price[key]]
# print(sum(result))

letters = [('AEILNORSTU', 1), ('DG', 2), ('BCMP', 3),
           ('FHVWY', 4), ('K', 5), ('JX', 8), ('QZ', 10)]
my_d = [dict.fromkeys(*elem) for elem in letters]
# print([() for i in range(7)])
# dict_my = dict()
# print(dict_)
print(letters)
print(my_d)





