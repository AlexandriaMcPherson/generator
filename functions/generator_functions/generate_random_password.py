import string
from random import choice

def generate_random_password(seed, rows, length=8):
    generated_data = []
    for i in range(rows):
        password = ""
        password += choice(string.ascii_uppercase) + choice(string.ascii_lowercase) + choice(string.digits) + choice(string.punctuation)
        for j in range(length - 4):
            password += choice(string.ascii_letters)
        generated_data.append(password)
    return generated_data