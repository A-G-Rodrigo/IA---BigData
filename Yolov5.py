#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 19:01:30 2023

@author: alvaro
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 12:21:54 2023

@author: alvaro
"""
import sys
sys.path.append('/home/alvaro/anaconda3/lib/python3.9/site-packages/yolov5')
import cv2
import subprocess
import timeit
from yolov5 import detect

def detecta_caras():
    
    #subprocess.call(["python", "/home/alvaro/anaconda3/lib/python3.9/site-packages/yolov5/detect.py", "--source", "0"])
    return detect.run()
t=timeit.repeat(detecta_caras,repeat=1,number=1)
print("Tiempo detección", t)
'''
# Cargamos el modelo de detección de YOLOv5
#yolo_detector = detect(weights='yolov5s.pt', threshold=0.5)

# Iniciamos la cámara
cap = cv2.VideoCapture(0)

while True:
    # Leemos un frame de la cámara
    ret, frame = cap.read()

    # Detección de caras utilizando YOLOv5
    bboxes = yolo_detector.detect(frame, ['face'])

    # Dibujamos el bounding box en el frame
    for bbox in bboxes:
        x1, y1, x2, y2, conf, cls = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Mostramos el frame en una ventana
    cv2.imshow('frame', frame)

    # Salimos del bucle si se presiona 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Liberamos los recursos utilizados
cap.release()
cv2.destroyAllWindows()
'''