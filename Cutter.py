def run():

    file=r'data/q.mp4'
    # file=r'test.mp4'

    start_time=37
    end_time=start_time+2

    cut_file(file,start_time,end_time)

def cut_file(file,start_time,end_time,output_file=None):

    import os

    path = os.getcwd()

    input_video='{}/{}'.format(path,file)

    # cutting a clip

    duration=end_time-start_time

    # setting clip name
    if not output_file:
        output_file=input_video.replace('.mp4','_cutted.mp4')

    # saving clip
    os.system("ffmpeg -y -ss {} -i {} -c copy -t {} {}".format(start_time,input_video,duration,output_file))

if __name__ == "__main__":
    run()
 