#DATASET: fashion_mnist
import tensorflow as tf
from tensorflow import keras #Keras is an library provided by tensorflow to import labeled image dataset.
import numpy as np
import matplotlib.pyplot as plt

#To load dataset from keras
dataset = keras.datasets.fashion_mnist

#splitting dataset into traing and testing
(train_images,train_labels),(test_images,test_labels) = dataset.load_data()

#shape of the dataset
print(train_images.shape)#(60000, 28, 28)
print(train_labels.shape)#(60000,)

print(test_images.shape)#(10000, 28, 28)
print(test_labels.shape)#(10000,)


class_name = class_names = ["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]
# plt.figure()
# plt.imshow(train_images[4])
# plt.show()

#converting RGB images to Gray Scale image
#0-255 into 0-1
train_images = train_images/255
test_images = test_images/255


#create neural network(Model)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),#Input layer
    keras.layers.Dense(128,activation='relu'),#Hidden Layer
    keras.layers.Dense(10,activation='softmax')#output layer
])

#to use optimizer and loss function and accuracy
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])


#Train the model
model.fit(train_images,train_labels, epochs=10)
#epochs/iteration it looks for dataset for training(on every iteration loss will minimized and accuracy maximized)


