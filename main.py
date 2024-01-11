import sys
import pandas as pd

from functions.check_args import check_args
from functions.generate_data import generate_data
from functions.parse_data_types import parse_data_types

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
        exit()

    # コラム名をリストにする
    column_names = input_df.columns.tolist()
    output_df = pd.DataFrame(columns=column_names)

    # コラムのデータ型を取得する
    input_data_types = input_df.iloc[0].to_list()
    try:
        data_types = parse_data_types(column_names, input_data_types)
    # 解析できない場合は、データを作成せずに終了
    except ValueError as e:
        print(e)
        print("データを作成できませんでした。")
        exit()

    # コラムごとにデータを作成する
    for column in data_types:
        column_data = generate_data(num_rows, column["type"], column["args"], rand_seed)
        # データフレームに入れる
        output_df[column["column_name"]] = column_data
        
    # .csvを出力する
    output_filename = input_filename[:-4] + "_data.csv"
    output_df.to_csv(path_or_buf=output_filename)
    print(output_filename + "を作成しました。")

if __name__ == "__main__":
    main()
