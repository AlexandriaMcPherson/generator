def check_args(args):
    if len(args) < 3:
        print("Usage: generator <number> <filename>.csv")
        exit()
    if not args[1].isnumeric():
        print("Usage: generator <number> <filename>.csv")
        exit()
    if args[2][-4:] != ".csv":
        print("Usage: generator <number> <filename>.csv")
        exit()