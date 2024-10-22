call_stack = []


def get_combin(n: int, k: int) -> int:
    call_stack.append(locals())
    print(call_stack)
    if k == 0 or k == n:
        return 1
    total = get_combin(n - 1, k) + get_combin(n - 1, k - 1)
    call_stack.pop()
    print(call_stack)
    return total


get_combin(4, 2)
