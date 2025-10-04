from collections import deque

my_deck_1 = deque([1, 2, 3])
print(my_deck_1)  # deque([1, 2, 3])
my_deck_1.pop()
print(my_deck_1)  # deque([1, 2])
my_deck_1.popleft()
print(my_deck_1)  # deque([2])
my_deck_1.popleft()
print(my_deck_1)  # deque([])
print()

my_deck = deque()
my_deck.popleft() # IndexError: pop from an empty deque
