def generate_zero_padded(rows, start, length):
    generated_rows = []
    for i in range(rows):
        next = start + i
        str_next = str(next)
        if len(str_next) < length:
            zeroes = ""
            for i in range(length - len(str_next)):
                zeroes += "0"
            str_next = zeroes + str_next
        generated_rows.append(str_next)
    return generated_rows