from random import seed
from random import random

def generate_random_zero_padded(rand_seed, rows, length, start, end, interval=None):
    if rand_seed is not None:
        seed(rand_seed)
    generated_rows = []
    if interval is not None:
        for i in range(rows):
            next = random.randrange(start, end, interval)
            str_next = str(next)
            if len(str_next) < length:
                zeroes = ""
                for i in range(length - len(str_next)):
                    zeroes += "0"
                str_next = zeroes + str_next
            generated_rows.append(str_next)
    else:
        for i in range(rows):
            next = random.randint(start, end)
            str_next = str(next)
            if len(str_next) < length:
                zeroes = ""
                for i in range(length - len(str_next)):
                    zeroes += "0"
                str_next = zeroes + str_next
            generated_rows.append(str_next)
    return generated_rows