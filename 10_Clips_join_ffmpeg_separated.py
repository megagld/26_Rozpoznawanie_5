import os

# directory/folder path
dir_path = 'cuts/_separated'

# list to store files
input_paths = []

# Iterate directory
for file_path in os.listdir(dir_path):
    # check if current file_path is a file
    if os.path.isfile(os.path.join(dir_path, file_path)):
        # add filename to list
        input_paths.append(f'{dir_path}/{file_path}')

open('concat.txt', 'w').writelines([('file %s\n' % input_path) for input_path in input_paths])

os.system("ffmpeg -f concat -i concat.txt -c copy ./cuts/_separated/all.mp4")