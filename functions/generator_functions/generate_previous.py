import pandas as pd

def generate_previous(dataframe, column_name):
    return dataframe[column_name].tolist()