from functions.generator_functions.generate_enum import generate_enum
from functions.generator_functions.generate_from_table import generate_from_table
from functions.generator_functions.generate_one import generate_one
from functions.generator_functions.generate_blank import generate_blank
from functions.generator_functions.generate_null import generate_null
from functions.generator_functions.generate_random import generate_random
from functions.generator_functions.generate_random_price import generate_random_price
from functions.generator_functions.generate_serial import generate_serial
from functions.generator_functions.generate_timestamp_date import generate_timestamp_date
from functions.generator_functions.generate_timestamp_millis import generate_timestamp_millis
from functions.generator_functions.generate_timestamp_now import generate_timestamp_now
from functions.generator_functions.generate_timestamp_seconds import generate_timestamp_seconds
from functions.generator_functions.generate_timestamp_today import generate_timestamp_today
from functions.generator_functions.generate_value import generate_fixed_value
from functions.generator_functions.generate_zero import generate_zero
from functions.generator_functions.generate_zero_padded import generate_zero_padded


def generate_data(rows, key, args=None, seed=None):
    match key:
        case "VALUE":
            return generate_fixed_value(rows, args[0])
        case "SERIAL":
            return generate_serial(rows, args[0])
        case "BLANK":
            return generate_blank(rows)
        case "FROM_TABLE":
            if len(args) < 2:
                repeat = False if args[2] == "FALSE" else True
                return generate_from_table(rows, args[0], args[1], repeat)
            else:
                return generate_from_table(rows, args[0], args[1])
        case "NULL":
            return generate_null(rows)
        case "ZERO":
            return generate_zero(rows)
        case "ONE":
            return generate_one(rows)
        case "RANDOM":
            if len(args) < 2:
                return generate_random(seed, rows, args[0], args[1], args[2])
            else:
                return generate_random(seed, rows, args[0], args[1])
        case "ZERO_PADDED":
            return generate_zero_padded(rows, args[0], args[1])
        case "RANDOM_ZERO_PADDED":
            return generate_zero_padded(rows, args[0], args[1])
        case "RANDOM_PRICE":
            if len(args) < 2:
                return generate_random_price(seed, rows, args[0], args[1], args[2])
            else:
                return generate_random_price(seed, rows, args[0], args[1])
        case "ENUM":
            return generate_enum(seed, rows, args)
        case "NAME_FULL":
            pass
        case "DATE_OF_BIRTH":
            pass
        case "SEX":
            pass
        case "TIMESTAMP_NOW":
            return generate_timestamp_now(rows)
        case "TIMESTAMP_TODAY":
            return generate_timestamp_today(rows)
        case "TIMESTAMP_DATE":
            return generate_timestamp_date(seed, rows, args[0], args[1])
        case "TIMESTAMP_SECONDS":
            return generate_timestamp_seconds(seed, rows, args[0], args[1])
        case "TIMESTAMP_MILLIS":
            return generate_timestamp_millis(seed, rows, args[0], args[1])