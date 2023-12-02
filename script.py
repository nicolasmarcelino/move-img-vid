import shutil
import os
import string
import random

'''
Warning: the script assumes the directories already exist
'''

def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

image_file_formats = (".jpg", ".gif", ".jpeg", ".png", ".webp")
video_file_formats = (".mp4", ".avi", ".mkv", ".flv", ".webm")

files = [f for f in os.listdir() if os.path.isfile(f) and (f.endswith(image_file_formats) or f.endswith(video_file_formats))]
progress = len(files)
# check the number of tracked files
# print(progress)

for file in files:
    file_name, file_extension = os.path.splitext(file)
    if file.endswith(image_file_formats):
        shutil.move(file, ''.join(('pics/', id_generator(), file_extension)))
    elif file.endswith(video_file_formats):
        shutil.move(file, ''.join(('vids/', id_generator(), file_extension)))
    else:
        print("something wrong with ", file)
    progress = progress - 1
    print(progress," files to go")
