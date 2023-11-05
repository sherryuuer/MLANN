import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

# create model
Weights = tf.Variable(tf.random.uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

@tf.function
def cost(W, b):
    y = Weights*x_data + biases
    error = tf.reduce_mean(tf.square(y - y_data))
    return error

# loss = tf.reduce_mean(tf.square(y-y_data))


optimizer = tf.optimizers.SGD(learning_rate=0.5)
trainable_vars = [Weights, biases]

for step in range(201):
    with tf.GradientTape() as tp:
        # your loss/cost function must always be contained within the gradient tape instantiation
        cost_fn = cost(Weights, biases)
    gradients = tp.gradient(cost_fn, trainable_vars)
    optimizer.apply_gradients(zip(gradients, trainable_vars))
    if step % 20 == 0:
        print(step, tf.print(Weights), tf.print(biases))






# from stackoverflow
# import numpy as np
# import tensorflow as tf
# from tensorflow import keras

# x_train = [1, 2, 3]
# y_train = [1, 2, 3]

# W = tf.Variable(tf.random.normal([1]), trainable = True, name='weight')
# b = tf.Variable(tf.random.normal([1]), trainable = True, name='bias')

# @tf.function
# def cost(W, b):
#     y_model = W * x_train + b
#     error = tf.reduce_mean(tf.square(y_train - y_model))
#     return error


# optimizer = tf.optimizers.SGD(learning_rate=0.01)

# trainable_vars = [W,b]

# epochs = 100 #(or however many iterations you want it to run)
# for _ in range(epochs):
#     with tf.GradientTape() as tp:
#         #your loss/cost function must always be contained within the gradient tape instantiation
#         cost_fn = cost(W, b)
#     gradients = tp.gradient(cost_fn, trainable_vars)
#     optimizer.apply_gradients(zip(gradients, trainable_vars))

# tf.print(W)
# tf.print(b)
