from random import choice


people, friends = [input() for _ in range(int(input()))], []
for person in people:
    friend = choice(list(set(people).difference(friends + [person])))
    friends.append(friend)
    print(f'{person} - {friend}')

