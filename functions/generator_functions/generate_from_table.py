from ..get_data_functions.get_data_from_table import get_data_from_table

def generate_from_table(rows, filename, column_name, repeat=True):
    data = get_data_from_table(filename, column_name)
    if repeat is True:
        while len(data) < rows:
            data += data
    else:
        null_vals = ["NULL" for i in range(rows - len(data))]
        data += null_vals
    if len(data) > rows:
        data = data[:rows]
    return data