from functions.generator_functions.generate_datetime import generate_datetime

from functions.random_gen import TIMESTAMP_DATE

def generate_timestamp_date(rand_seed, rows, start, end):
    timestamps = generate_datetime(rand_seed, rows, start, end)
    res = []
    # Convert to string
    for ts in timestamps:
        res.append(ts.strftime(TIMESTAMP_DATE))
    return res