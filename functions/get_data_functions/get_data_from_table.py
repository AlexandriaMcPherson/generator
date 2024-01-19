import pandas as pd

def get_data_from_table(filename, column_name):
    df = pd.DataFrame()
    # Read column from CSV into list
    try:
        df = pd.read_csv(filename)
    except:
        print("インポートデータエラー：ファイルを読み込めませんでした。")
    # Check column name
    if column_name not in df.columns:
        print("インポートデータエラー：コラム名が見つかれませんでした。")
    # Fill missing values with NULL
    df[column_name] = df[column_name].fillna("NULL")
    data = df[column_name].tolist()
    return data