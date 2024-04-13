import time


# Мой вариант решения быстрее...
# def spell(*args):
#     words = sorted([w.lower() for w in args], key=len, reverse=True)
#     answer = {}
#     for word in words:
#         answer.setdefault(word[0], len(word))
#     return answer

# Второй вариант решения (преподавателя)
def spell(*args):
    result = {}
    for word in args:
        if result.get(word[0].lower(), 0) < len(word):
            result[word[0].lower()] = len(word)
    return result


start = time.time()
for _ in range(1):
    words = ['Россия', 'Австрия', 'Австралия',
            'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

    spell(*words)
    spell('Математика', 'История', 'химия', 'биология', 'Информатика')
    words = ['fruit', 'football', 'February', 'forest', 'Family']
    spell(*words)
    spell()
finish = time.time()
print(finish - start)