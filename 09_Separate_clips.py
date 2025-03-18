import os
import shutil

# directory/folder path
dir_path = 'cuts//_frames'

# list to store files
clips = []

# Iterate directory
for file_path in os.listdir(dir_path):
    # check if current file_path is a file
    if os.path.isfile(os.path.join(dir_path, file_path)):
        # add filename to list
        clips.append(f'{file_path.replace('jpg','mp4')}')


for clip in clips:
    dir_path=os.getcwd()
    file_from='{}\\cuts\\{}'.format(dir_path,clip)
    file_to='{}\\cuts\\_separated\\{}'.format(dir_path,clip)

    shutil.copy2(file_from, file_to)