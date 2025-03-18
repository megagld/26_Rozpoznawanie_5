import os

# os.system("ffmpeg -i ./cuts/_separated/all.mp4 -c:v libx264 -preset slow -crf 23 -c:a aac -b:a 160k -vf format=yuv420p -movflags +faststart ./cuts/_separated/all_encoded.mp4")

# ffmpeg -i all.mp4 -vcodec libx265 -crf 28 output_3.mp4



import os

# directory/folder path
dir_path = 'E:/_cuts'
ready_path = 'E:/_gotowe'



for path,_,files in os.walk(dir_path):
    for file in files:
        file_name='{}/{}'.format(dir_path, file)
        ready_file_name='{}/{}'.format(ready_path, file)
        print(ready_file_name)
        os.system(f"ffmpeg -i {file_name} -c:v libx264 -preset slow -crf 23 -c:a aac -b:a 160k -vf format=yuv420p -movflags +faststart {ready_file_name}")

 