from datetime import datetime, timedelta
import random

DAYS_IN_YEAR = 365
DAYS_IN_MONTH = 30
HOURS_IN_DAY = 24
MINS_IN_HOUR= 60
SECONDS_IN_MIN = 60
MILLIS_IN_SECOND = 1000
TIMESTAMP_WITH_MICROS='%Y-%m-%d %H:%M:%S.%f'
TIMESTAMP_WITH_SECONDS='%Y-%m-%d %H:%M:%S'
TIMESTAMP_DATE='%Y-%m-%d'

# ---Personal Information---
# Names
# Addresses
# Phone Numbers
# Emails
# Birthdate

# ---Time---
def dt_to_ts_millis(dt):
    ts = dt.strftime(TIMESTAMP_WITH_MICROS)[:-3]
    return ts


def dt_to_date(dt):
    ts = dt.strftime(TIMESTAMP_DATE)
    return ts


def timedelta_1day():
    random_hour = random.randint(0, HOURS_IN_DAY)
    random_min = random.randint(0, MINS_IN_HOUR)
    random_second = random.randint(0, SECONDS_IN_MIN)
    random_milli = random.randint(0, MILLIS_IN_SECOND)
    td = timedelta(hours = random_hour, minutes = random_min, seconds= random_second, milliseconds=random_milli)
    return td


def timedelta_1month():
    random_days = random.randint(0, DAYS_IN_MONTH)
    td = timedelta(days= random_days)
    return td


def timedelta_1year():
    random_days = random.randint(0, DAYS_IN_YEAR)
    td = timedelta(days= random_days)
    return td


def rand_timestamp_1year_yyyymmddhhmmss():
    td = timedelta_1day() + timedelta_1year()
    dt = datetime.now() - td
    ts = dt_to_ts_millis(dt)
    return ts


def rand_timestamp_1year_yyyymmdd():
    td = timedelta_1year()
    dt = datetime.now() - td
    ts = dt_to_date(dt)
    return ts


def rand_timestamp_1month_yyyymmddhhmmss():
    td = timedelta_1day() + timedelta_1month()
    dt = datetime.now() - td
    ts = dt_to_ts_millis(dt)
    return ts


def rand_timestamp_1month_yyyymmdd():
    td = timedelta_1month()
    dt = datetime.now() - td
    ts = dt_to_date(dt)
    return ts


def rand_timestamp_series_yyyymmddhhmmss(start_date, end_date, number):
    # Check that number can be generated safely
    # Get time period in unix time seconds
    # Generate x random numbers between those times
    # Convert to timestamp
    # Output
    pass


# Date this year
# Date this month
# Date with hh:mm:ss

# ---Numbers---
# Serial in range
# Single digit in range
# Number with leading 0s
# 10,000s

# ---Actions/Enums---
# Function that takes a list and spits out a random answer

# ---Files/Data---
# Filename
# File data
# URL