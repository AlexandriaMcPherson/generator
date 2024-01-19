import random
from ..get_data_functions.get_data_from_table import get_data_from_table

def generate_random_from_table(rows, filename, column_name):
    import_data = get_data_from_table(filename, column_name)
    generated_data = []
    for i in range(rows):
        generated_data.append(random.choice(import_data))
    return generated_data