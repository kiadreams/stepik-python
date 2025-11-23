from collections import deque

my_deck_1 = deque([5, 9, 3, 6, 8])
print('Стартовое состояние:', my_deck_1)  # Стартовое состояние: deque([5, 9, 3, 6, 8])
my_deck_1.rotate()
print(my_deck_1)  # deque([8, 5, 9, 3, 6])
my_deck_1.rotate(2)
print(my_deck_1)  # deque([3, 6, 8, 5, 9])
print()

my_deck = deque([5, 9, 3, 6, 8])
print('Старт:', my_deck)  # Старт: deque([5, 9, 3, 6, 8])
my_deck.rotate(-1)
print(my_deck)  # deque([9, 3, 6, 8, 5])
my_deck.rotate(-2)
print(my_deck)  # deque([6, 8, 5, 9, 3])
