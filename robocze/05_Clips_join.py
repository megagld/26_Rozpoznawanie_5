from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

# directory/folder path
dir_path = 'cuts'

# list to store files
res = []

# Iterate directory
for file_path in os.listdir(dir_path):
    # check if current file_path is a file
    if os.path.isfile(os.path.join(dir_path, file_path)):
        # add filename to list
        res.append(file_path)

res=[VideoFileClip(f'cuts/{i}') for i in res]

# # Concat cuts
final = concatenate_videoclips(res)

# # Write output to the file
final.write_videofile("cuts/all.mp4")