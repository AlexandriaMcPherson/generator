from random import seed
from random import random

def generate_random(rand_seed, rows, start, end, interval=None):
    if rand_seed is not None:
        seed(rand_seed)
    if interval is not None:
        return [random.randrange(start, end, interval) for i in range(rows)]
    else:
        return [random.randint(start, end) for i in range(rows)]