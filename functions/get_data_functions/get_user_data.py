from pandas import DataFrame
from ..data.user_data_colnames import user_data_colnames

def get_user_data(rows, column, user_df):
    df = user_df.head(rows).copy()
    return df[user_data_colnames[column]].to_list()