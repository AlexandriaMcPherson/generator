from collections import OrderedDict
import pandas as pd

from functions.read_txt_file_to_dict import read_txt_file_to_dict

def read_txt_file_to_df(filename):
    data_dict = read_txt_file_to_dict(filename)
    df = pd.DataFrame([data_dict])
    return df
        