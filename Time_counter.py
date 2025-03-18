from moviepy.editor import *
import os
import time
from datetime import datetime
import os


def save_time(start_time,file_name,input_video):
    ex_time=int(time.time() - start_time)

    # input_video='data/cut.mp4'

    # input video
    cap = VideoFileClip(input_video)

    fps_value = cap.fps
    frames_count=cap.reader.nframes
    cap_size=cap.size
    file_size=round(os.stat(input_video).st_size/ (1024 * 1024),2)
    
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    text_to_save=f'{dt_string}: {ex_time}[s]   -   {round(frames_count/ex_time,1)}[frames/s]    -   {cap_size}[size]  -   {fps_value}[fps]   -   {frames_count}[frames]    -   {file_size}[file size MB]  -   {file_name}\n'

    with open('time_ex.txt', 'a') as f:
        f.write(text_to_save)