from typing import List, Optional


def get_first_repeated_word(words: List[str]) -> Optional[str]:
    """Находит первый дубль в списке"""
    other_words = []
    for el in words:
        if el in other_words:
            return el
        else:
            other_words.append(el)
    else:
        return None


print(get_first_repeated_word(['ab', 'ca', 'bc', 'ca', 'ab', 'bc']))