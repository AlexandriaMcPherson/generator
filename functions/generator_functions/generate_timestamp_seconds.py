from functions.generator_functions.generate_datetime import generate_datetime

from functions.random_gen import TIMESTAMP_WITH_SECONDS

def generate_timestamp_seconds(rand_seed, rows, start, end):
    timestamps = generate_datetime(rand_seed, rows, start, end)
    # Convert to string
    for ts in timestamps:
        ts = ts.strftime(TIMESTAMP_WITH_SECONDS)