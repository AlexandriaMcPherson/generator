import sys

def check_args(args):
    usage = "使い方: generator.py <int 行数> <str ファイル名>.csv <int シード>"
    if len(args) < 3:
        print(usage)
        sys.exit(1)
    if not args[1].isnumeric():
        print(usage)
        sys.exit(1)
    if args[2][-4:] not in [".csv", ".txt"]:
        print(usage)
        sys.exit(1)
    if len(args) > 3 and args[3].isnumeric() == False:
        print(usage)
        sys.exit(1)