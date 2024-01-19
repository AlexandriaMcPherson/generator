from datetime import datetime

from functions.random_gen import TIMESTAMP_DATE, TIMESTAMP_WITH_MICROS, TIMESTAMP_WITH_SECONDS

def check_column_args_num(data_type, args):
    match data_type:
        case "VALUE" | "COPY":
            if not args or len(args) != 1:
                return False
            else:
                return True
        case "SERIAL" | "ID":
            if args and len(args) > 1:
                return False
            return True
        case "FROM_TABLE" | "RANDOM_FROM_TABLE" |"RANDOM" | "RANDOM_PRICE" | "ZERO_PADDED" | "RANDOM_ZERO_PADDED" | "ENUM" | "LIST_ORD" | "LIST_RAND" | \
            "TIMESTAMP" | "TIMESTAMP_DATE" | "TIMESTAMP_SECONDS" | "TIMESTAMP_MILLIS":
            if len(args) < 2:
                return False
            else:
                return True
        case _:
            return True
        
def check_column_args_valid(data_type, args):
    match data_type:
        case "SERIAL" | "ID":
            if not args[0].isnumeric():
                return False
            return True
        case "FROM_TABLE" | "RANDOM_FROM_TABLE": 
            if args[0][-4:] != ".csv":
                return False
            return True
        case "RANDOM" | "RANDOM_PRICE" | "ZERO_PADDED" | "RANDOM_ZERO_PADDED":
            for arg in args:
                if not arg.isnumeric():
                    return False
            return True
        case "TIMESTAMP" | "TIMESTAMP_DATE" | "TIMESTAMP_SECONDS" | "TIMESTAMP_MILLIS":
            for arg in args:
                if len(arg) > 18:
                    timeformat = TIMESTAMP_WITH_MICROS
                elif len(arg) > 10:
                    timeformat = TIMESTAMP_WITH_SECONDS
                else:
                    timeformat = TIMESTAMP_DATE
                try:
                    parse_ts = datetime.strptime(arg, timeformat)
                except ValueError:
                    return False
            return True
        case _:
            return True
        

def check_column_args(column_name, data_type, args):
    if args:
        num_error = f'Incorrect number of args for {column_name} of type {data_type}.'
        invalid_error = f'Incorrect type of args for {column_name} of type {data_type}.'
        if not check_column_args_num(data_type, args):
            print(num_error)
            return False
        if not check_column_args_valid(data_type, args):
            print(invalid_error)
            return False
    return True
    