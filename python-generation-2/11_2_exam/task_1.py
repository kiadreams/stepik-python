result = {'GCTA'[i]: 'CGAU'[i] for i in range(4)}
print(*(result[k] for k in input()), sep='')
