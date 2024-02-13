#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 17:32:01 2023

@author: alvaro
"""
# Se cargan las librerías necesarias

import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image

# Se carga el modelo guardado con anterioridad

model = load_model('./horse_or_human2.h5')

# Se crea la variable path con la ruta de la imagen

#path = './horse-or-human/train/horses/horse01-0.png'
#path = './horse-or-human/train/horses/horse01-0.png'
#path = './horse-or-human/train/humans/human01-01.png'
#path = './humano.jpeg'
#path = './humano2.jpeg'
#path = './humano3.jpeg'
#path = './caballo10.jpeg'
path = './caballo9.jpeg'

# Se carga y se procesa la imagen para ser tratada por el método predict()

img = image.load_img(path, target_size=(300, 300))
x = image.img_to_array(img)
#print(x)
x = np.expand_dims(x, axis=0)
images = np.vstack([x])

# Se ejecuta una predicción en base al modelo

classes = model.predict(images, batch_size=10)
#print(path)
#print(classes)
if classes[0][0] == 1:
    print("Es un caballo")
else:
    print("Es un humano")