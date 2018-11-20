import cv2
import time
from pathlib import Path
import os

path = str(Path.home())
i=0
try:
    os.mkdir(path+'/.image')
except: pass

while True:
    i+=1
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    name = path + '/.image/img' + str(i) + '.png'
    cv2.imwrite(name,frame)
    cap.release()
    cv2.destroyAllWindows()
    time.sleep(5)

