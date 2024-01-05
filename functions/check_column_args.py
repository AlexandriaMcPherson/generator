def check_column_args(column_name, data_type, args):
    error = f'Incorrect args for ${column_name} of type ${data_type}.'
    match data_type:
        case "VALUE":
            if len(args) != 1:
                print(error)
                return True
        case "SERIAL":
            if len(args) != 1:
                print(error)
                return True
        case "RANDOM":
            if len(args) < 2:
                print(error)
                return True
        case "ZERO_PADDED":
            if len(args) < 2:
                print(error)
                return True
        case "ENUM":
            if len(args) < 2:
                print(error)
                return True
        case _:
            return False