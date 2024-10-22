def get_arith_progression(a1, d, n):
    if n == 1:
        return a1
    return d + get_arith_progression(a1, d, n - 1)


print(get_arith_progression(10, -3, 5))