def generate_serial(rows, start):
    generated_rows = []
    for num in range(start, (start + rows)):
        generated_rows.append(num)
    return generated_rows