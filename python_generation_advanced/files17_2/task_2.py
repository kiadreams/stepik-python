f = open(input(), encoding='utf-8')
print(f.readlines()[-2].rstrip())
f.close()