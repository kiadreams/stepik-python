from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().rounding = ROUND_HALF_UP

*goods, discount = map(Decimal, [input() for _ in range(int(input()) + 1)])
discount_goods = map(
    lambda x: (x * (1 - discount)).quantize(Decimal('1e-2')), goods
)
print(sum(discount_goods))
