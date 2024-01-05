import pandas as pd

def generate_from_table(rows, filename, column_name, repeat=True):
    pass
    # Read column from CSV into list
    try:
        df = pd.read_csv(filename)
    except:
        print("Could not read file.")
    # Check column name
    if column_name not in df.columns:
        print("Column name not found.")
    # Fill missing values with NULL
    df[column_name] = df[column_name].fillna("NULL")
    data = df[column_name].tolist()
    if repeat is True:
        while len(data) < rows:
            data += data
    else:
        null_vals = ["NULL" for i in range(rows - len(data))]
        data += null_vals
    if len(data) > rows:
        data = data[:rows]
    return data