import cv2
cap = cv2.VideoCapture("data/VID_20241203_122956_resized.mp4")
print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
cap.set(cv2.CAP_PROP_POS_FRAMES, 18240)
res, frame = cap.read()
while 1:

    cv2.imshow("input", frame)
    key = cv2.waitKey(10)
    if key == 27:
        break
