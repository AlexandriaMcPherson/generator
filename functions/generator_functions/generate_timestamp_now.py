import datetime

from functions.random_gen import dt_to_ts_millis

def generate_timestamp_now(rows):
    dt_now = datetime.now()
    timestamp = dt_to_ts_millis(dt_now)
    return [timestamp for i in range(rows)]