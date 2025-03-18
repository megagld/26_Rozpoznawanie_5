import subprocess
import os
import filedate

def make_frame(folder_path,file):
    video_input_path = f'{folder_path}\\cuts\\{file}'

    subprocess.call(['ffmpeg', '-an', '-ss', '00:00:01.500', '-i', video_input_path, '-vframes', '1', '-vf', 
                    'scale=800:800:force_original_aspect_ratio=increase', '-f', 'mjpeg', '-y', f'{folder_path}\\cuts\\_frames\\{file.replace('mp4','jpg')}'])
    
def run():
    folder_path = os.getcwd()
    for path,_,files in os.walk('cuts'):
        for file in files:
            if file[-4:]=='.mp4' and not '_frames' in path:
                make_frame(folder_path,file)


if __name__ == "__main__":
    run()