import re

from functions.check_column_args import check_column_args
from functions.check_data_type import check_data_type

def parse_data_types(column_names, data_types):
    data_types_dict = {}
    errors = []
    # Capture type
    for i in range(len(data_types)):
        type_string = str(data_types[i])
        data_type = ""
        args = []
        pattern = re.compile(r'^[^(]*')
        capture_group = pattern.search(type_string)
        if capture_group:
            data_type = capture_group.group(0)
        else:
            data_type = type_string
        if not data_type:
            # Return error
            print("コラム" + column_names[i] + "にて" + str(data_types[i]) + "というデータ型が解析できませんでした。")
            errors.append(True)
            continue
        if not check_data_type(data_type):
            print("コラム" + column_names[i] + "にて" + data_type + "というデータ型が解析できませんでした。")
            errors.append(True)
            continue
        # Capture args
        # pattern = re.compile(r'\(([^,]+(?:,\s*[^,]+)*)\)')
        args_string = type_string.replace(data_type, "") # Remove data type from front of string
        args_string = args_string[1:-2] # Remove parentheses from beginning and end
        args_string.replace("\"", "") # Remove quotation marks
        if args_string:
            # result = args_string.group(1)
            args = [e.strip() for e in args_string.split(' ')]
            errors.append(True if not check_column_args(column_names[i], data_type, args) else False)
        else:
            args = None
        data_types_dict.update({i: {"column_name": column_names[i], "type": data_type, "args": args}})
        # match type_string.upper():
        #     case "VALUE":
        #         errors.append(check_column_args(column_names[i], "VALUE", args))
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "VALUE", "args": args}})
        #     case "SERIAL":
        #         errors.append(check_column_args(column_names[i], "SERIAL", args))
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "SERIAL", "args": args}})
        #     case "BLANK":
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "BLANK", "args": None}})
        #     case "NULL":
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "NULL", "args": None}})
        #     case "ZERO":
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "ZERO", "args": None}})
        #     case "ONE":
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "ONE", "args": None}})
        #     case "RANDOM":
        #         errors.append(check_column_args(column_names[i], "RANDOM", args))
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "RANDOM", "args": args}})
        #     case "RANDOM_PRICE":
        #         errors.append(check_column_args(column_names[i], "RANDOM_PRICE", args))
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "RANDOM_PRICE", "args": args}})
        #     case "ZERO_PADDED":
        #         errors.append(check_column_args(column_names[i], "ZERO_PADDED", args))
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "ZERO_PADDED", "args": args}})
        #     case "ENUM":
        #         errors.append(check_column_args(column_names[i], "ENUM", args))
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "ENUM", "args": args}})
        #     case "NAME_FULL":
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "NAME_FULL", "args": None}})
        #     case "DATE_OF_BIRTH":
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "DATE_OF_BIRTH", "args": None}})
        #     case "SEX":
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "SEX", "args": None}})
        #     case "ADDRESS_ZIP":
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "ADDRESS_ZIP", "args": None}})
        #     case "ADDRESS_FULL":
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "ADDRESS_FULL", "args": None}})
        #     case "TIMESTAMP_NOW":
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "TIMESTAMP_NOW", "args": None}})
        #     case "TIMESTAMP_TODAY":
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "TIMESTAMP_TODAY", "args": None}})
        #     case "TIMESTAMP_DATE":
        #         errors.append(check_column_args(column_names[i], "TIMESTAMP_DATE", args))
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "TIMESTAMP_DATE", "args": args}})
        #     case "TIMESTAMP_SECONDS":
        #         errors.append(check_column_args(column_names[i], "TIMESTAMP_SECONDS", args))
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "TIMESTAMP_SECONDS", "args": args}})
        #     case "TIMESTAMP_MILLIS":
        #         errors.append(check_column_args(column_names[i], "TIMESTAMP_MILLIS", args))
        #         data_types_dict.update({i: {"column_name": column_names[i], "type": "TIMESTAMP_MILLIS", "args": args}})
        
    for error in errors:
        if error:
            raise ValueError("コラムを構文解析中にエラーが発生しました。")
    return data_types_dict