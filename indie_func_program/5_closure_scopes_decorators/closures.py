def count_calls():

    def _counter():
        _counter.total_calls += 1

    _counter.total_calls = 0
    return _counter


# !!!ВТОРОЙ ВАРИАНТ!!!
# def count_calls():
#     total_calls = 0
#
#     def _counter():
#         nonlocal total_calls
#         total_calls += 1
#         setattr(_counter, "total_calls", total_calls)
#
#     setattr(_counter, "total_calls", total_calls)
#     return _counter


counter1 = count_calls()
counter2 = count_calls()
counter1()
print(counter1.total_calls, counter2.total_calls)
counter1()
counter2()
print(counter1.total_calls, counter2.total_calls)
counter2()
counter2()
print(counter1.total_calls, counter2.total_calls)
