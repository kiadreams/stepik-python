import random

def generate_ip():
    some_ip = [str(random.randrange(256)) for _ in range(4)]
    return '.'.join(some_ip)
