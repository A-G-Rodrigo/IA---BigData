import tensorflow as tf
import numpy as np
mnist =  tf.keras.datasets.mnist
(x_train,y_train), (x_test, y_test) = mnist.load_data()

# Visualizar datos previa normalización
#print(x_train[0])
#print(y_test)
#print(x_test)
print(y_train.size)
print(x_train.size)
# Normalización de los datos cargados
y_train = tf.cast(np.array(y_train/255))
x_train = tf.cast(np.array(x_train/255))
#print(x_train[0])
print(np.array(y_train.shape))
print(y_test.shape)
print(x_train.shape)
print(x_test.shape)
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(256, activation="relu"))
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dense(10, activation="softmax"))

model.compile(loss = 'binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#model.evaluate(np.array(x_test), np.array(y_test))
model.fit(x_train, y_train, epochs=5)