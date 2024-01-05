import re

from functions.check_column_args import check_column_args
from functions.check_data_type import check_data_type

def parse_data_types(column_names, data_types):
    data_types_dict = {}
    errors = []
    # Capture type
    for i in range(len(data_types)):
        type = ""
        args = []
        pattern = re.compile(r'^.*?\(')
        capture_group = pattern.search(data_types[i])
        if capture_group:
            type = capture_group.group(0)
        if not type:
            # Return error
            print("コラム" + column_names[i] + "にて" + data_types[i] + "というデータ型が解析できませんでした。")
            errors.append(True)
            continue
        if not check_data_type(type):
            print("コラム" + column_names[i] + "にて" + type + "というデータ型が解析できませんでした。")
            errors.append(True)
            continue
        # Capture args
        pattern = re.compile(r'\(([^,]+(?:,\s*[^,]+)*)\)')
        args_string = pattern.search(data_types[i])
        if args_string:
            result = args_string.group(1)
            args = [e.strip() for e in result.split(',')]
        match data_types[i].upper():
            case "VALUE":
                errors.append(check_column_args(column_names[i], "VALUE", args))
                data_types_dict.update({i: {"column_name": column_names[i], "type": "VALUE", "args": args}})
            case "SERIAL":
                errors.append(check_column_args(column_names[i], "SERIAL", args))
                data_types_dict.update({i: {"column_name": column_names[i], "type": "SERIAL", "args": args}})
            case "BLANK":
                data_types_dict.update({i: {"column_name": column_names[i], "type": "BLANK", "args": None}})
            case "NULL":
                data_types_dict.update({i: {"column_name": column_names[i], "type": "NULL", "args": None}})
            case "ZERO":
                data_types_dict.update({i: {"column_name": column_names[i], "type": "ZERO", "args": None}})
            case "ONE":
                data_types_dict.update({i: {"column_name": column_names[i], "type": "ONE", "args": None}})
            case "RANDOM":
                errors.append(check_column_args(column_names[i], "RANDOM", args))
                data_types_dict.update({i: {"column_name": column_names[i], "type": "RANDOM", "args": args}})
            case "ZERO_PADDED":
                errors.append(check_column_args(column_names[i], "ZERO_PADDED", args))
                data_types_dict.update({i: {"column_name": column_names[i], "type": "ZERO_PADDED", "args": args}})
            case "ENUM":
                errors.append(check_column_args(column_names[i], "ENUM", args))
                data_types_dict.update({i: {"column_name": column_names[i], "type": "ENUM", "args": args}})
            case "NAME_FULL":
                data_types_dict.update({i: {"column_name": column_names[i], "type": "NAME_FULL", "args": None}})
            case "DATE_OF_BIRTH":
                data_types_dict.update({i: {"column_name": column_names[i], "type": "DATE_OF_BIRTH", "args": None}})
            case "SEX":
                data_types_dict.update({i: {"column_name": column_names[i], "type": "SEX", "args": None}})
        
        for error in errors:
            if error:
                raise ValueError("コラムを構文解析中にエラーが発生しました。")
    return data_types_dict