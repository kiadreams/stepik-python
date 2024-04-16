import decimal

num = decimal.Decimal(input())
symbols = sorted(num.as_tuple().digits)
print((abs(num) > 1) * symbols[0] + symbols[-1])
