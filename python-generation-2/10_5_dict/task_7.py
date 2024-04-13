words = ['hello', 'bye', 'yes', 'no', 'python',
         'apple', 'maybe', 'stepik', 'beegeek']

result = {key: list(map(ord, key)) for key in words}
