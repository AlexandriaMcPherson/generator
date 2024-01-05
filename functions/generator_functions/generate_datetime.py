from random import random
import datetime

from functions.random_gen import TIMESTAMP_DATE, TIMESTAMP_WITH_SECONDS, TIMESTAMP_WITH_MICROS

def generate_datetime(rand_seed, rows, start, end):
    if rand_seed is not None:
        random.seed(rand_seed)
    # Get start and end in unix time
    if len(start) < 17:
        timeformat = TIMESTAMP_WITH_MICROS
    elif len(start) < 8:
        timeformat = TIMESTAMP_WITH_SECONDS
    else:
        timeformat = TIMESTAMP_DATE
    start_unix = int(round(datetime.strptime(timeformat, start).timestamp()))
    end_unix = int(round(datetime.strptime(timeformat, end).timestamp()))
    timestamps = []
    for i in range(rows):
        ts = random.randint(start_unix, end_unix)
        # Convert timestamp to datetime
        timestamp = datetime.utcfromtimestamp(ts)
        timestamps.append(timestamp)
    # Sort timestamps
    timestamps.sort()
    return timestamps