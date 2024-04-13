from string import digits as ds

is_non_negative_n_1 = lambda n: n.count('.') < 2 and not set(n) - set(ds + '.')


is_non_negative_num = lambda n: n.replace('.', '', 1).strip().isdigit()

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))




