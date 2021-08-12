import tensorflow as tf
import numpy as np
from tensorflow import keras

import matplotlib.pyplot as plt

# load data (60k training, 10k testing; 70k total)
(train_images, train_labels), (test_images, test_labels) = keras.datasets.fashion_mnist.load_data()

print(train_images[59999]) # 784 pixel values!
print(train_labels[59999])
plt.imshow(train_images[59999], cmap='gray', vmin=0, vmax=255)
plt.show()

model = keras.Sequential([
    # input layer: 28x28 flattened to 784x1
    keras.layers.Flatten(input_shape = (28,28)), 

    # hidden layer: 128 nodes, relu returns value of every node in layer
    keras.layers.Dense(units=128, activation=tf.nn.relu),

    # output layer: 0-9, dense connects all nodes from previous layer to this one
    # units is how many nodes in our layer
    # activation: the tf method to return the "final" output of the layer
    keras.layers.Dense(units=10, activation=tf.nn.softmax)
    ]
)

# compile keras nn to prepare it for training
model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# train
model.fit(train_images, train_labels, epochs=5)

# test 
test_loss = model.evaluate(test_images, test_labels)

# visualize trained nn on test data
plt.imshow(test_images[0])
plt.show()
print("Expected Classification:", test_labels[0])

# predict
predictions = model.predict(test_images)
print("Predictions for first image:", predictions[0])

