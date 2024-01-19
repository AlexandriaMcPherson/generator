import random

def generate_enum(rand_seed, rows, items):
    if rand_seed is not None:
        random.seed(rand_seed)
    return [random.choice(items) for i in range(rows)]