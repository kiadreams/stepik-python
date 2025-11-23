import sys
from collections import Counter

counter = Counter()
while (line := sys.stdin.readline()).strip().lower() != 'end':
    counter.update(line.lower().strip().split())
for k, v in counter.items():
    print(f'{k}: {v}')




