import re

from functions.check_column_args import check_column_args
from functions.check_data_type import check_data_type

def parse_data_types(column_names, data_types):
    data_types_dict = dict()
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
        args_string = type_string.replace(data_type, "") # Remove data type from front of string
        args_string = args_string[1:-1] # Remove parentheses from beginning and end
        args_string = args_string.replace("\"", "") # Remove quotation marks
        if args_string:
            args = [e.strip() for e in args_string.split(" ")]
            errors.append(True if not check_column_args(column_names[i], data_type, args) else False)
        else:
            args = None
        data_types_dict.update({i: {"column_name": column_names[i], "type": data_type, "args": args}})
        
    for error in errors:
        if error:
            raise ValueError("コラムを構文解析中にエラーが発生しました。")
    return data_types_dict