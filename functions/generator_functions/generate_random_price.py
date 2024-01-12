from random import seed
import random

def generate_random_price(rand_seed, rows, start, end, interval=None):
    pass
    if rand_seed is not None:
        seed(rand_seed)
    if interval is not None:
        return [str(random.randrange(int(start), int(end), int(interval))) + ".000" for i in range(rows)]
    else:
        return [str(random.randint(int(start), int(end))) + ".000" for i in range(rows)]