from random import seed
import random

def generate_random(rand_seed, rows, start, end, interval=None):
    if rand_seed is not None:
        seed(rand_seed)
    if interval is not None:
        return [random.randrange(int(start), int(end), int(interval)) for i in range(rows)]
    else:
        return [random.randint(int(start), int(end)) for i in range(rows)]