import random
import string


result = set()
while len(result) < 100:
    number = str(random.randint(1, 9)) + ''.join(random.sample(string.digits, 6))
    result.add(number)
print(*result, sep='\n')
