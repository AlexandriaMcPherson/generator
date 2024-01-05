from datetime import datetime

from functions.random_gen import TIMESTAMP_DATE, TIMESTAMP_WITH_MICROS, TIMESTAMP_WITH_SECONDS

def check_column_args(column_name, data_type, args):
    error = f'Incorrect args for ${column_name} of type ${data_type}.'
    # Check number of args
    match data_type:
        case "VALUE" | "SERIAL":
            if len(args) != 1:
                print(error)
                return True
        case "FROM_TABLE" | "RANDOM" | "RANDOM_PRICE" | "ZERO_PADDED" | "ENUM" | "TIMESTAMP_DATE" | \
        "TIMESTAMP_SECONDS" | "TIMESTAMP_MILLIS":
            if len(args) < 2:
                print(error)
                return True
        case _:
            return False
        
    # Check args valid
    match data_type:
        case "SERIAL":
            if not args[0].isnumeric():
                print(error)
                return True
            return False
        case "FROM_TABLE": 
            if args[0][-4:] != ".csv":
                print(error)
                return True
            return False
        case "RANDOM" | "RANDOM_PRICE" | "ZERO_PADDED":
            for arg in args:
                if not arg.isnumeric():
                    print(error)
                    return True
            return False
        case "TIMESTAMP_DATE" | "TIMESTAMP_SECONDS" | "TIMESTAMP_MILLIS":
            # TODO Check timestamp validity
            for arg in args:
                    if len(arg) < 17:
                        timeformat = TIMESTAMP_WITH_MICROS
                    elif len(arg) < 8:
                        timeformat = TIMESTAMP_WITH_SECONDS
                    else:
                        timeformat = TIMESTAMP_DATE
                    try:
                        parse_ts = datetime.strptime(arg, timeformat)
                    except ValueError:
                        print(error)
                        return True
            return False
        case _:
            return False