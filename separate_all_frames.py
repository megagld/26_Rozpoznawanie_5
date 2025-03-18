import subprocess
import os
import filedate
import cv2

# def make_frame(folder_path,file):
#     video_input_path = f'{folder_path}\\cuts\\{file}'

#     subprocess.call(['ffmpeg', '-an', '-ss', '00:00:01.500', '-i', video_input_path, '-vframes', '1', '-vf', 
#                     'scale=800:800:force_original_aspect_ratio=increase', '-f', 'mjpeg', '-y', f'{folder_path}\\cuts\\_frames\\{file.replace('mp4','jpg')}'])
    
# def run():
#     folder_path = os.getcwd()
#     for path,_,files in os.walk('cuts'):
#         for file in files:
#             if file[-4:]=='.mp4' and not '_frames' in path:
#                 make_frame(folder_path,file)



# if __name__ == "__main__":
#     run()

main_dir = os.getcwd()

file = 'VID_20250226_134010_008.mp4'

source = f'data\\{file}'

cap = cv2.VideoCapture(source)

cnt=1

while(cap.isOpened): #loop until cap opened or video not complete

        ret, frame = cap.read()  #get frame and success from video capture
        
        if ret: #if success is true, means frame exist
            orig_image = frame #store frame

            output_frame_file = "{}\\{}_{:03d}.jpg".format(
                'cuts\\_frames',
                file.replace(".mp4", ""),
                cnt
            )


            # try:
            #     cv2.imshow("input", orig_image)
            # except:
            #     pass

            # if orig_image is None:
            #     break

            # if cv2.waitKey(1) == ord('q'):
            #     break
            
            cv2.imwrite(output_frame_file, orig_image)

            cnt+=1
        else:
            pass
