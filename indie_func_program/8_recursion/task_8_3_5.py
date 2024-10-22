def get_arith_progression(n):
    if n == 1:
        return 1
    return 7 + get_arith_progression(n - 1)


print(get_arith_progression(2))