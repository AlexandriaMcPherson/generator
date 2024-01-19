from functions.generator_functions.generate_enum import generate_enum
from functions.generator_functions.generate_from_table import generate_from_table
from functions.generator_functions.generate_ip_address import generate_ip_address
from functions.generator_functions.generate_previous import generate_previous
from functions.generator_functions.generate_random_from_table import generate_random_from_table
from functions.generator_functions.generate_one import generate_one
from functions.generator_functions.generate_blank import generate_blank
from functions.generator_functions.generate_null import generate_null
from functions.generator_functions.generate_ordered_list import generate_ordered_list
from functions.generator_functions.generate_random import generate_random
from functions.generator_functions.generate_random_password import generate_random_password
from functions.generator_functions.generate_random_price import generate_random_price
from functions.generator_functions.generate_random_zero_padded import generate_random_zero_padded
from functions.generator_functions.generate_serial import generate_serial
from functions.generator_functions.generate_timestamp_date import generate_timestamp_date
from functions.generator_functions.generate_timestamp_millis import generate_timestamp_millis
from functions.generator_functions.generate_timestamp_now import generate_timestamp_now
from functions.generator_functions.generate_timestamp_seconds import generate_timestamp_seconds
from functions.generator_functions.generate_timestamp_today import generate_timestamp_today
from functions.generator_functions.generate_user_agent import generate_user_agent
from functions.generator_functions.generate_value import generate_fixed_value
from functions.generator_functions.generate_zero import generate_zero
from functions.generator_functions.generate_zero_padded import generate_zero_padded

from functions.get_data_functions.get_user_data import get_user_data
from functions.get_data_functions.get_full_name import get_full_name
from functions.get_data_functions.get_sex_as_num import get_sex_as_num


def generate_data(dataframe, rows, key, args=None, seed=None, pregenerated_data=None):
    match key:
        case "VALUE":
            return generate_fixed_value(rows, args[0])
        case "SERIAL" | "ID":
            if args:
                return generate_serial(rows, args[0])
            else:
                return generate_serial(rows) 
        case "BLANK":
            return generate_blank(rows)
        case "FROM_TABLE":
            if len(args) < 2:
                repeat = False if args[2] == "FALSE" else True
                return generate_from_table(rows, args[0], args[1], repeat)
            else:
                return generate_from_table(rows, args[0], args[1])
        case "RANDOM_FROM_TABLE":
            return generate_random_from_table(rows, args[0], args[1])
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
            return generate_random_zero_padded(rows, args[0], args[1])
        case "RANDOM_PRICE":
            if len(args) < 2:
                return generate_random_price(seed, rows, args[0], args[1], args[2])
            else:
                return generate_random_price(seed, rows, args[0], args[1])
        case "LIST_RAND" | "ENUM":
            return generate_enum(seed, rows, args)
        case "LIST_ORD":
            return generate_ordered_list(rows, args)
        case "PREVIOUS" | "COPY":
            return generate_previous(dataframe, args[0])
        case "USERNAME":
            raise NotImplementedError
        case "PASSWORD_RANDOM":
            if args:
                return generate_random_password(seed, rows, args[0])
            else:
                return generate_random_password(seed, rows)
        case "PASSWORD_HASH":
            raise NotImplementedError
        case "NAME_FAMILY":
            return get_user_data(rows, "last_name", pregenerated_data)
        case "NAME_FIRST":
            return get_user_data(rows, "first_name", pregenerated_data)
        case "NAME_FULL":
            return get_full_name(rows, pregenerated_data)
        case "DATE_OF_BIRTH":
            return get_user_data(rows, "date_of_birth", pregenerated_data)
        case "SEX":
            return get_user_data(rows, "sex", pregenerated_data)
        case "SEX_AS_NUM":
            return get_sex_as_num(rows, pregenerated_data)
        case "ADDRESS_ZIP":
            return get_user_data(rows, "zip_code", pregenerated_data)
        case "ADDRESS_FULL":
            return get_user_data(rows, "address", pregenerated_data)
        case "COMPANY_NAME":
            return get_user_data(rows, "company", pregenerated_data)
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
        case "USER_AGENT":
            return generate_user_agent(seed, rows)
        case "IP_ADDRESS":
            return generate_ip_address(seed, rows)