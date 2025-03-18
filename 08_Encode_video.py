import os

os.system("ffmpeg -i ./cuts/all.mp4 -c:v libx264 -preset slow -crf 23 -c:a aac -b:a 160k -vf format=yuv420p -movflags +faststart ./cuts/all_encoded.mp4")

