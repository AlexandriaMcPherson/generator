from pandas import DataFrame
from ..data.user_data_colnames import user_data_colnames

def get_full_name(rows, user_df):
    df = user_df.head(rows).copy()
    df["fullname"] = df[user_data_colnames["last_name"]] + df[user_data_colnames["first_name"]]
    return df["fullname"].to_list()[:rows]