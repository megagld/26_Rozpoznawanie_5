import subprocess
import os
import filedate

def make_thumbnail(folder_path,file):
    video_input_path = f'{folder_path}\\cuts\\{file}'

    subprocess.call(['ffmpeg', '-an', '-ss', '00:00:01.500', '-i', video_input_path, '-vframes', '1', '-vf', 
                    'scale=800:800:force_original_aspect_ratio=increase', '-f', 'mjpeg', '-y', f'{folder_path}\\cuts\\.@__thumb\\s800{file}'])
    
    subprocess.call(['ffmpeg', '-i', f'{folder_path}\\cuts\\.@__thumb\\s800{file}', '-vf', 'scale=260:260:force_original_aspect_ratio=decrease',
                    '-f', 'mjpeg', '-y', f'{folder_path}\\cuts\\.@__thumb\\s100{file}'])
    
    subprocess.call(['ffmpeg', '-i', f'{folder_path}\\cuts\\.@__thumb\\s800{file}', '-vf', 'scale=400:400:force_original_aspect_ratio=decrease',
                    '-f', 'mjpeg', '-y', f'{folder_path}\\cuts\\.@__thumb\\default{file}'])
    

    files_to_update=[video_input_path,
                     f'{folder_path}\\cuts\\.@__thumb\\s100{file}',
                     f'{folder_path}\\cuts\\.@__thumb\\s800{file}',
                     f'{folder_path}\\cuts\\.@__thumb\\default{file}']

    time_to_set=os.path.getctime(video_input_path)

    for file_to_update in files_to_update:
        filedate.File(file_to_update).set(
            created = time_to_set,
            modified = time_to_set,
            accessed = time_to_set)


def run():
    folder_path = os.getcwd()
    for path,_,files in os.walk('cuts'):
        for file in files:
            if file[-4:]=='.mp4' and not '.@__thumb' in path:
                make_thumbnail(folder_path,file)


if __name__ == "__main__":
    run()