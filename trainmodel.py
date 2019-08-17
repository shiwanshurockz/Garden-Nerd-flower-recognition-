

from keras.callbacks import EarlyStopping, ModelCheckpoint
import keras
import numpy as np
from keras import backend as k
from keras.models import Sequential
from keras.layers import Activation
from keras.layers import LeakyReLU
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from sklearn.metrics import confusion_matrix
from keras.layers.convolutional import *
import itertools
from keras.layers.core import Dropout
from keras.callbacks import ModelCheckpoint
from keras.layers import LeakyReLU
from keras.layers import Dense, GlobalAveragePooling2D, Dropout
from keras.models import Model

model = keras.applications.inception_v3.InceptionV3(include_top = True, weights=None, input_tensor=None, input_shape=(256,256,3), pooling= 'max', classes=102)


model.summary()


train_path = 'D:\\WORK\\hackerearth Challenge\\flower\\final segmented_image\\my_data\\train'
valid_path = 'D:\\WORK\\hackerearth Challenge\\flower\\final segmented_image\\my_data\\val'


train_batches = ImageDataGenerator(samplewise_center=True, rotation_range=30, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, vertical_flip=True, rescale=1./255).flow_from_directory(
    train_path, target_size=(256, 256), batch_size=8,class_mode='categorical')
valid_batches = ImageDataGenerator(samplewise_center=True, rotation_range=30, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, vertical_flip=True, rescale=1./255).flow_from_directory(
    valid_path, target_size=(256, 256), batch_size=4, class_mode='categorical')


learning = 0.0001
model.compile(Adam(lr = learning, decay = 0.00002), loss='categorical_crossentropy',
              metrics=['accuracy'])
model.load_weights('withoutclass3.h5')

early_stop = EarlyStopping(
    monitor='val_loss', min_delta=0.00001, patience=20, mode='min', verbose=1)
checkpoint = ModelCheckpoint('withoutclass4.h5', monitor='val_loss',
                             verbose=1, save_best_only='True', mode='min', period=1)


model.fit_generator(train_batches, steps_per_epoch=2070, validation_data=valid_batches,
                    validation_steps=475, epochs=20, verbose=2, callbacks=[early_stop, checkpoint])