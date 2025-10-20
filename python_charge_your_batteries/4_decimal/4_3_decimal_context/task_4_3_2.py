from decimal import Decimal, getcontext

n = Decimal(2)
for i in range(3, 52):
    getcontext().prec = i
    print(n.sqrt())
