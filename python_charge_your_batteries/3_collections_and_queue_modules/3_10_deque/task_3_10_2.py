from collections import deque
from string import punctuation


def is_palindrome(s: str) -> bool:
    deq = deque(x for x in s.lower() if x not in punctuation + ' ')
    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False
    return True


assert is_palindrome("A man, a plan, a canal, Panama") is True
assert is_palindrome("race car") is True
assert is_palindrome("hello") is False
