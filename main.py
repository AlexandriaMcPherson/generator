import sys
import pandas as pd

from functions.check_args import check_args
from functions.generate_data import generate_data
from functions.parse_data_types import parse_data_types
from functions.data_type_list import data_type_list
from constants import PREGENERATED_DATA
from constants import REQUIRES_USER_DATA

def main():
    # 引数を確認する
    check_args(sys.argv)
    num_rows = int(sys.argv[1])
    input_filename = sys.argv[2]
    if len(sys.argv) > 3:
        rand_seed = int(sys.argv[3])
    else:
        rand_seed = None
    
    # ファイルをデータフレームに読み込む
    try:
        input_df = pd.read_csv(input_filename, keep_default_na=False) # NULLを文字列として扱う
    except:
        print("ファイルを読み込めませんでした。")
        sys.exit(1)

    # コラム名をリストにする
    column_names = input_df.columns.tolist()
    output_df = pd.DataFrame()

    # コラムのデータ型を取得する
    input_data_types = input_df.iloc[0].to_list()
    try:
        data_types = parse_data_types(column_names, input_data_types)
    # 解析できない場合は、データを作成せずに終了
    except ValueError as e:
        print(e)
        print("データを作成できませんでした。")
        sys.exit(1)

    # Check if requested data types require user data and open file
    list_data_types = [val["type"] for col, val in data_types.items()]
    if not REQUIRES_USER_DATA.isdisjoint(list_data_types):
        user_df = pd.read_csv(PREGENERATED_DATA)
        if num_rows > 10000:
            print("エラー：ユーザーデータは10,000行までです。")
            sys.exit(1)
    else:
        user_df = None

    # コラムごとにデータを作成する
    for col_num, column in data_types.items():
        column_data = generate_data(output_df, num_rows, column["type"], column["args"], rand_seed, user_df)
        # データフレームに入れる
        output_df[column["column_name"]] = column_data
        
    # .csvを出力する
    output_filename = input_filename[:-4] + "_data.csv"
    output_df.to_csv(path_or_buf=output_filename, index=False)
    print(output_filename + "を作成しました。")

if __name__ == "__main__":
    main()
