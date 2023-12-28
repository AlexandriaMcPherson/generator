import sys
import pandas as pd
import functions.check_args as check_args
import functions.parse_data_types as parse_data_types

def main():
    # Get filename and number of rows to generate from args
    check_args(sys.argv)
    num_rows = int(sys.argv[1])
    input_filename = sys.argv[2]
    # Read file into dataframe
    try:
        input_df = pd.read_csv(input_filename)
    except:
        print("Could not read file.")
    # For each column, get column name
    column_names = input_df.columns.tolist()
    output_df = pd.DataFrame(columns=column_names)
    # For each column, parse data type
    input_data_types = input_df.iloc[0]
    data_types = parse_data_types(input_data_types)
    for i in range(len(input_data_types)):
        # Parse data type and parameters
        pass
    # Generate data
    for i in range(num_rows):
        for j in range(len(data_types.keys())):
            # Generate each column
            pass
    # Insert into dataframe
    # Output csv
    output_df.to_csv()

if __name__ == "__main__":
    main()
