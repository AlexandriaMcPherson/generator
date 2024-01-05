import datetime

from functions.random_gen import dt_to_date

def generate_timestamp_today(rows):
    dt_now = datetime.now()
    timestamp = dt_to_date(dt_now)
    return [timestamp for i in range(rows)]