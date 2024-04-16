import time


def for_and_append():            # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result

def list_comprehension():        # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]

start = time.monotonic()

# result = for_and_append()
# print(len(result))
result = list_comprehension()
print(len(result))

finish = time.monotonic()
print(finish - start)