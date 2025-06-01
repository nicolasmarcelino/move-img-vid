import os

strings = []

files = os.listdir()

print(type(len(files)))

files.remove("script.py")

for index in range(len(files)):
    filename, file_extension = files[index].rsplit('.', 1)
    new_filename = ".".join([strings[index], file_extension])
    os.rename(files[index], new_filename)
