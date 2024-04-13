from decimal import Decimal as D


num = D(input())
result = num.sqrt() + num.exp() + num.log10() + num.ln()
print(result)
