import moviepy.editor as mp
import os
from wakepy import keep

def resize_video(file,path):

    clip = mp.VideoFileClip('{}/{}'.format(path,file))
    clip_resized = clip.resize(height=384).without_audio() # make the height 360px and remove audio ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
    clip_resized.write_videofile(f"{path}/{file}_resized.mp4".replace('.mp4_','_'),fps=15)
    

with keep.running() as k:
    # do stuff that takes long time

    for i,j,k in os.walk('data'):
        for l in k:
            resized_file_name=l.replace('.mp4','_resized.mp4')
            if l.endswith('.mp4') and not l.endswith('resized.mp4') and not resized_file_name in k:
                resize_video(l,i)
