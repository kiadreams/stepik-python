from collections import deque, Counter


numbers = deque(map(int, input().split()))
players = Counter()
count = 0
while numbers:
    match count % 2:
        case 0:
            players['A'] += numbers.popleft()
        case 1:
            players['B'] += numbers.pop()
    count += 1
if players['A'] == players['B']:
    print('DRAW')
else:
    print('FIRST' if players['A'] > players['B'] else 'SECOND')
