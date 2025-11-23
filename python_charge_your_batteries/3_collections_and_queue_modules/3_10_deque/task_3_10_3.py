from collections import deque


numbers = deque(map(int, input().split()))
for _ in range(int(input())):
    command, side, *args = input().split()
    match command:
        case 'A':
            num = int(args[0])
            numbers.appendleft(num) if side == 'L' else numbers.append(num)
        case 'D':
            numbers.popleft() if side == 'L' else numbers.pop()
        case 'R':
            numbers.rotate(-1 if side == 'L' else 1)
print(numbers)
