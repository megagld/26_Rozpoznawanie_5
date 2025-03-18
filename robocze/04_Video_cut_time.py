from moviepy.editor import *
import json
import os
from openpyxl import load_workbook, Workbook


def cut_vid(file,path):

    clip = VideoFileClip(f'{path}\\{file}')

    # getting data from xlsx
   
    path = os.getcwd()
    xlsx_file='{}/data/times.xlsx'.format(path)

    wb=load_workbook(xlsx_file)
    ws = wb['cuts']
 
    video_cuts=[]

    for i in ws.values:

        if i[0]!='file' and i[0]==file[:-4]:
            count=i[1]
            start_time=i[2]
            end_time=i[3]
            start_cor=i[4]*1000 if i[4] else 0
            end_cor=i[5]*1000 if i[5] else 0
            if i[6]!='x':
                video_cuts.append([count,start_time+start_cor,end_time+end_cor])

    wb.close()
    
    # cutting a clip

    for c,i,j in video_cuts:
        start_time,end_time=i,j

        # setting clip name
        clip_name='cuts/{}_{:03d}.mp4'.format(file.replace('.mp4',''),c)

        # setting a start and end time
        start_time=max(0,(start_time-1000)/1000)
        end_time=min((end_time+2000)/1000,clip.duration)

        # saving clip
        clip_tmp=clip.subclip(start_time,end_time)
        clip_tmp.write_videofile(clip_name,codec='libx264')


for i,j,k in os.walk('data'):
    for l in k:
        if all( (l.endswith('.mp4'), not l.endswith('resized.mp4'))):
            cut_vid(l,i)