import os
import random

characters = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

def generate_random_string():
    return ''.join(random.choice(characters) for _ in range(16))

files = os.listdir()

files.remove("script.py")

strings = [generate_random_string() for _ in range(len(files))]

for index in range(len(files)):
    filename, file_extension = files[index].rsplit('.', 1)
    new_filename = ".".join([strings[index], file_extension])
    os.rename(files[index], new_filename)
