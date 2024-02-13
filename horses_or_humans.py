#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 19:05:19 2023

@author: alvaro
"""
# Se cargan las librerías necesarias

import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.image as mpimg
from keras_preprocessing.image import ImageDataGenerator

# Se crean variables donde almacenar las rutas hacia las imágenes

human_train = os.path.join('./horse-or-human/horse-or-human/train/humans')
horse_train = os.path.join('./horse-or-human/horse-or-human/train/horses')
human_validation = os.path.join('./horse-or-human/horse-or-human/validation/humans')
horse_validation = os.path.join('./horse-or-human/horse-or-human/validation/horses')

# Se comprueba el paso anterior

print('imagenes totales de humanos:', len(os.listdir(human_train)))
print('imagenes totales de caballos:', len(os.listdir(horse_train)))
horse_train_files = os.listdir(horse_train)
print(horse_train_files[:10])
human_train_files = os.listdir(human_train)
print(human_train_files[:10])

# Implementación de ImageDataGenerator 

TRAINING_DIR = './horse-or-human/horse-or-human/train'
training_datagen = ImageDataGenerator(
      rescale = 1./255,
	  rotation_range=40,
      width_shift_range=0.2,
      height_shift_range=0.2,
      shear_range=0.2,
      zoom_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest')

train_generator = training_datagen.flow_from_directory(
	TRAINING_DIR,
	target_size=(300,300),
	class_mode='categorical'
)

VALIDATION_DIR = './horse-or-human/horse-or-human/validation'
validation_datagen = ImageDataGenerator(
    rescale = 1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)


validation_generator = validation_datagen.flow_from_directory(
	VALIDATION_DIR,
	target_size=(300,300),
	class_mode='categorical'
)

# Creación del modelo

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(300, 300, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])

# Información del modelo 

model.summary()

# Compilación del modelo

model.compile(loss = 'categorical_crossentropy', 
              optimizer='rmsprop', 
              metrics=['accuracy'])

# Entrenamiento del modelo

history = model.fit(train_generator, 
                    epochs=20, 
                    validation_data = validation_generator, 
                    verbose = 1)

# Se guarda para poder trabajar con él

model.save("/home/alvaro/Escritorio/C/CEIA/PIA/UT4/Práctica_4.6_PIA_Álvaro_García_Rodrigo/horse_or_human2.h5")

# Se genera un gráfico con los valores de loss y accuracy 
# durante el entrenamiento y la validación

history.history.keys()
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(len(acc))
plt.plot(epochs, acc, 'r', label='precisión del entrenamiento')
plt.plot(epochs, val_acc, 'b', label='precisión de la validación')
plt.title('Precisión de entrenamiento y validación')
plt.legend(loc=0)
plt.figure()
plt.show()

# Con el modelo guardado, ejecutar el archivo 
# modelo_predicción_horse_or_human para hacer predicciones