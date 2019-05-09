from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import matplotlib.pyplot as plt

(train_images, train_labels),(test_images, test_labels) = mnist.load_data()

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
network.add(layers.Dense(10, activation="softmax"))

network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape(10000, 28*28)
test_images = test_images.astype('float32') / 255

print("before change:", test_labels[0])
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
print("after change:", test_labels[0])

network.fit(train_images, train_labels, epochs=1, batch_size=128)
test_loss, test_acc = network.evaluate(test_images, test_labels, verbose=1)
print('test_acc:', test_acc)



(train_images, train_labels),(test_images, test_labels) = mnist.load_data()
plt.imshow(test_images[10], cmap=plt.cm.binary)
plt.show()

test_images = test_images.reshape(10000, 28*28)
res = network.predict(test_images)
for i in range(res[0].shape[0]):
    if (res[10][i] == 1):
        print("the number for the picture is ", i)