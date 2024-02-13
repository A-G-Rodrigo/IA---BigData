#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 01:00:30 2023

@author: alvaro
"""

import numpy as np
import cv2 
import timeit

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
#eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eyes.xml')
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#glassesCascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        # Mide el tiempo que tarda el algoritmo en detectar una cara
    t = timeit.repeat(lambda: faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)), number=1)
    
    # Imprime el tiempo de detección de cara
    print(f'Tiempo de detección de cara: {t} segundos')
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30,30))
    print(' '+str(len(faces))+' caras')
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eyeCascade.detectMultiScale(
            roi_gray,
            scaleFactor = 1.5,
            minNeighbors=10,
            minSize=(5,5))

        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)    
            
        

    cv2.imshow('video', img)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
