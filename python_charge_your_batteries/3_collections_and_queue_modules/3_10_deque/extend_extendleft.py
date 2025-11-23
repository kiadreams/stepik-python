from collections import deque

my_deck_1 = deque([1, 2, 3])
print(my_deck_1)  # deque([1, 2, 3])
my_deck_1.extend((5, 6, 7))
print(my_deck_1)  # deque([1, 2, 3, 5, 6, 7])
my_deck_1.extendleft((8, 9, 10))
print(my_deck_1)  # deque([10, 9, 8, 1, 2, 3, 5, 6, 7])
print()

my_deck = deque([1, 2, 3], maxlen=5)
print(my_deck)  # deque([1, 2, 3], maxlen=5)
my_deck.extend((4, 5, 6))
print(my_deck)  # deque([2, 3, 4, 5, 6], maxlen=5)
my_deck.extendleft((7, 8, 9))
print(my_deck)  # deque([9, 8, 7, 2, 3], maxlen=5)
