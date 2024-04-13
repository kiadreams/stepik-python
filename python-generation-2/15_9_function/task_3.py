abscissas = [float(i) for i in input().split()]
ordinates = [float(i) for i in input().split()]
applicates = [float(i) for i in input().split()]
result = all(
    map(lambda x, y, z: x ** 2 + y ** 2 + z ** 2 <= 4,
        abscissas,
        ordinates,
        applicates)
)
print(result)