from random import randint
from .get_user_data import get_user_data

def get_sex_as_num(rows, user_df):
    data_list = get_user_data(rows, "sex", user_df)
    for item in data_list:
        if item == "男":
            item = 1
        elif item == "女":
            item = 2
        else:
            item = randint(1,2)