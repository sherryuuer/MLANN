import tensorflow as tf
import numpy as np
from tensorflow import keras
import os


# model
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# loss func and optimizer
model.compile(optimizer='sgd', loss='mean_squared_error')

# data
xs = np.array([-1, 0, 1, 2, 3, 4], dtype=float)
ys = np.array([-2, 1, 4, 7, 10, 13], dtype=float)

# train
model.fit(xs, ys, epochs=500)

# predict
print(f"Do some predictions: {model.predict([10])}")
