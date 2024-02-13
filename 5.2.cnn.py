import tensorflow as tf
import numpy as np
mnist =  tf.keras.datasets.mnist
(x_train,y_train), (x_test, y_test) = mnist.load_data()

# Visualizar datos previa normalización
#print(x_train[0])
#print(y_test)
#print(x_test)

# Normalización de los datos cargados
y_train = y_train/255
x_train = x_train/255
#print(x_train[0])
print(y_train)

# Crear la red
model = tf.keras.models.Sequential()

### Primera convolución
# 64 -> número de filtros, (3,3) -> tamaño del kernel,
model.add(tf.keras.layers.Conv2D(64, (3,3), input_shape = (x_train.reshape[1:]))) # Para la primera capa especificamos el tamaño de la entrada
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))

### Segunda Convolución
model.add(tf.keras.layers.Conv2D(64, (3,3)))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))

### Tercera Convolución
model.add(tf.keras.layers.Conv2D(64, (3,3)))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))

### Aplanar
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64))
model.add(tf.keras.layers.Activation("relu"))

### Cada densa
model.add(tf.keras.layers.Dense(32))
model.add(tf.keras.layers.Activation("relu"))

### Capa de salida (10 valores)
model.add(tf.keras.layers.Dense(10))
model.add(tf.keras.layers.Activation("softmax"))

model.compile(loss = 'binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, x_test, epochs=5)