#bmystek
import os
import io
import shutil
import tkinter as tk
import winsound
import regex as re
import time
from tkinter import ttk
import cv2
from ultralytics import YOLO
from ultralytics import YOLO
import cv2
import json
import os
from wakepy import keep
import time
from Time_counter import *
from tkinter import ttk
import winsound
import tkinter as tk
import math
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Alignment
import ffmpeg


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # root window
        row_c=7
        row_height=25
        cols=[150,250]
        prop=cols[0]//cols[1]

        root_width=sum(cols)
        root_height=row_c*row_height

        # root = tk.Tk()
        self.geometry('{}x{}'.format(root_width,root_height))
        self.title('Wyświetl klatkę')
        self.resizable(0, 0)
         
        # configure the grid
        self.columnconfigure(0, weight=prop)
        self.columnconfigure(1, weight=1)

        self.create_widgets()

    def run(self):    

        # pobiera dane z okienek
        self.file =       self.entry_state[3].get()
        self.frame =       int(self.entry_state[5].get())
        
        self.show_frame()

    def show_frame(self):

        print(self.frame)

        self.input_dir = os.getcwd()

        file_path=f'{self.input_dir}\\data\\{self.file}'

        # input video
        cap = cv2.VideoCapture(file_path)

        # model
        model = YOLO("yolo-Weights/yolov8n.pt")
        # model = YOLO("yolo11n.pt")
        

        print(file_path)

        cap.set(0,self.frame)
        res, img = cap.read()

        results = model.predict(source=img)
        
        classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
            "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
            "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
            "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
            "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
            "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
            "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
            "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
            "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
            "teddy bear", "hair drier", "toothbrush"
            ]

        # classNames=['bike', 'person', 'wheel','x','y','z','m','n']
        # coordinates
        for r in results:
            boxes = r.boxes

            for box in boxes:
                # class name
                cls = int(box.cls[0])
                print(cls)

                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

                # put box in cam
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # confidence
                confidence = math.ceil((box.conf[0]*100))/100

                                # object details
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2

                cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)

            try:
                cv2.imshow("input", img)
            except:
                pass

            if img is None:
                break

            if cv2.waitKey(1) == ord('q'):
                break


        pass

    def create_widgets(self):
        #set labels
        texts=['',
            '',
            '',
            'Plik:',
            '',
            'Klatka/czas [ms]:',
            '']
        self.texts_state={}

        for i,j in enumerate(texts):
            label = ttk.Label(self, text=j,font=('helvetica', 10))
            label.grid(column=0, row=i, sticky=tk.E, padx=5)
            self.texts_state[i]=label

        # set entry
        entrys=['',
            'button',
            '',
            '-',
            '',
            '-',
            '']
        self.entry_state={}

        for i,j in enumerate(entrys):
            if j=='':
                entry = ttk.Label(self, text=j,font=('helvetica', 10))
                entry.grid(column=0, row=i, sticky=tk.E, padx=5)
            elif j=='checkbox':
                self.var = tk.IntVar(value=1)
                entry=tk.Checkbutton(self,variable=self.var)
            elif j=='button':
                entry=tk.Button(text='Wyświetl klatkę', command=self.run, bg='brown', fg='white', font=('helvetica', 10, 'bold'),width=16)
            elif j=='progresbar':
                entry=ttk.Progressbar(self, orient='horizontal',mode='determinate', length=140)
            else:
                entry = ttk.Entry(self,textvariable='',width=30)
                entry.insert(-1, j)

            entry.grid(column=1, row=i, sticky=tk.W, padx=5)
            self.entry_state[i]=entry

    def parse_files(self):
        input_dir = os.getcwd()

        self.lista_plikow=[]

        for path,_,files in os.walk(input_dir):
            for mp4_file in files:
                if mp4_file.endswith(".mp4"):
                    self.lista_plikow.append([path.split('\\')[-1],mp4_file])

if __name__ == "__main__":
    app = App()
    app.mainloop()