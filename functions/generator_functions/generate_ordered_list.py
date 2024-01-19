def generate_ordered_list(rows, list_data):
    generated_data = []
    for i in range(rows):
        generated_data[i] = list_data[i % len(list_data)]
    return generated_data