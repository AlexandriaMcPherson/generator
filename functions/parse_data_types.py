import re

def parse_data_types(column_names, data_types):
    data_types_dict = {}
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
            print("Could not parse data type: " + data_types[i] + " in column " + column_names[i])
        # Capture args
        pattern = re.compile(r'\(([^,]+(?:,\s*[^,]+)*)\)')
        args_string = pattern.search(data_types[i])
        if args_string:
            result = args_string.group(1)
            args = [e.strip() for e in result.split(',')]
        match data_types[i].upper():
            case "VALUE":
                data_types_dict.update({i: {"column_name": column_names[i], "type": "VALUE", "args": args}})
            case "SERIAL":
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
                data_types_dict.update({i: {"column_name": column_names[i], "type": "RANDOM", "args": args}})
            case "ZERO_PADDED":
                data_types_dict.update({i: {"column_name": column_names[i], "type": "ZERO_PADDED", "args": args}})
            case "ENUM":
                data_types_dict.update({i: {"column_name": column_names[i], "type": "ENUM", "args": args}})
            case "NAME_FULL":
                data_types_dict.update({i: {"column_name": column_names[i], "type": "NAME_FULL", "args": None}})
            case "DATE_OF_BIRTH":
                data_types_dict.update({i: {"column_name": column_names[i], "type": "DATE_OF_BIRTH", "args": None}})
            case "SEX":
                data_types_dict.update({i: {"column_name": column_names[i], "type": "SEX", "args": None}})
    return data_types_dict