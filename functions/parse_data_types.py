import re

def parse_data_types(data_types):
    data_types_dict = {}
    # Capture type
    for data_type in data_types:
        type = ""
        args = []
        pattern = re.compile(r'^.*?\(')
        capture_group = pattern.search(data_type)
        if capture_group:
            type = capture_group.group(0)
        if not type:
            # Return error
            print("Could not parse data type: " + data_type)
        # Capture args
        pattern = re.compile(r'\(([^,]+(?:,\s*[^,]+)*)\)')
        args_string = pattern.search(data_type)
        if args_string:
            result = args_string.group(1)
            args = [e.strip() for e in result.split(',')]
        match data_type.upper():
            case "VALUE":
                data_types_dict.update({"VALUE": args})
            case "SERIAL":
                data_types_dict.update({"SERIAL": args})
            case "BLANK":
                data_types_dict.update({"BLANK": []})
            case "NULL":
                data_types_dict.update({"NULL": []})
            case "ZERO":
                data_types_dict.update({"ZERO": []})
            case "ONE":
                data_types_dict.update({"ONE": []})
            case "RANDOM":
                data_types_dict.update({"RANDOM": args})
            case "ZERO_PADDED":
                data_types_dict.update({"ZERO_PADDED": args})
            case "ENUM":
                data_types_dict.update({"ENUM": args})
            case "NAME_FULL":
                data_types_dict.update({"NAME_FULL": []})
            case "DATE_OF_BIRTH":
                data_types_dict.update({"DATE_OF_BIRTH": []})
            case "SEX":
                data_types_dict.update({"SEX": []})
    return data_types_dict