def check_args(args):
    usage = "使い方: generator.py <int 行数> <str ファイル名>.csv <int シード>"
    if len(args) < 3:
        print(usage)
        exit()
    if not args[1].isnumeric():
        print(usage)
        exit()
    if args[2][-4:] != ".csv":
        print(usage)
        exit()
    if len(args > 3) and args[3].isnumeric() == False:
        print(usage)
        exit()