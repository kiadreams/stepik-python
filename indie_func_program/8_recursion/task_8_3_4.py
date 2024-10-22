def is_palindrome(s: str):
    if len(s) in (0, 1):
        return True
    elif s[0].lower() == s[-1].lower():
        return is_palindrome(s[1:-1])
    return False


print(is_palindrome('Racecar'))


print(is_palindrome('abba'))
