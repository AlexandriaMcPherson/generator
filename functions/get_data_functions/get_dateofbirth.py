from pandas import DataFrame
from user_data_colnames import DOB

def get_last_name(rows, user_df):
    df = user_df.head(rows)
    return df[DOB].to_list()