from collections import deque


values, window_size = map(int, input().split()), int(input())
deq = deque(maxlen=window_size)
for n in values:
    deq.append(n)
    if len(deq) == window_size:
        print(max(deq), end=' ')
