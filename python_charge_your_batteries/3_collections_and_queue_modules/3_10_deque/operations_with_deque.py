from collections import deque

my_deck = deque([7, 1, 9, 3, 5])
print(my_deck)  # deque([7, 1, 9, 3, 5])
print('Get index of 0', my_deck[0])  # Get index of 0 7
print('Get index of 2', my_deck[2])  # Get index of 2 9
print('Get index of -1', my_deck[-1])  # Get index of -1 5

print('Sum is', sum(my_deck))  # Sum is 25
print('Len is', len(my_deck))  # Len is 5
print('Maximum is', max(my_deck))  # Maximum is 9
print('Minimum is', min(my_deck))   # Minimum is 1
print('9 in my_deck? ', 9 in my_deck)   # True
print('8 in my_deck? ', 8 in my_deck)   # False

lst = list(my_deck)
tpl = tuple(my_deck)

for i in my_deck:
    print(i)

print(my_deck + deque('abc'))  # deque([7, 1, 9, 3, 5, 'a', 'b', 'c'])
print(my_deck * 2)  # deque([7, 1, 9, 3, 5, 7, 1, 9, 3, 5])
