import os
from sklearn import model_selection
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.inception_v3 import InceptionV3
from keras.layers import Flatten, Dense, Dropout,MaxPooling2D,GlobalAveragePooling2D,Input
import matplotlib as plt
from keras.models import Sequential
from keras.optimizers import adam, SGD,Adagrad,adadelta,RMSprop
import sklearn.model_selection 
import pickle
from keras.models import Model  

train_dir = ('C:/Users/gordo/OneDrive/Desktop/Python_Projects/flowers')
test_dir = ('C:/Users/gordo/OneDrive/Desktop/Python_Projects/flowers_test')


def image_gen_w_aug(train_parent_directory, test_parent_directory):
    train_data = ImageDataGenerator(
        rescale=1/255,
        rotation_range=30,
        zoom_range=0.2,
        width_shift_range=0.1,
        height_shift_range=0.1,
        validation_split=0.15
        )
    
    train_generator =train_data.flow_from_directory(
        train_parent_directory,
        target_size=(75,75),
        batch_size=214,
        classes=['daisy','dandelion','rose','sunflower','tulip'],
        class_mode='categorical',
        subset='training'
        )

    val_generator = train_data.flow_from_directory(
        train_parent_directory,
        target_size=(75,75),
        batch_size=37,
        classes=['daisy','dandelion','rose','sunflower','tulip'],
        class_mode='categorical',
        subset='training'
        )
    test_generator = train_data.flow_from_directory(
        test_parent_directory,
        target_size=(75,75),
        batch_size=37,
        classes=['daisy','dandelion','rose','sunflower','tulip'],
        class_mode='categorical'
        )
    return train_generator,val_generator,test_generator


train_generator,val_generator,test_generator = image_gen_w_aug(train_dir,test_dir)

def model_output(pre_trained_model,last_output):
    x = Flatten()(last_output)
    x = Dense(512,activation='relu')(x)
    x = Dropout(0.2)(x)
    x = Dense(5,activation='softmax')(x)

    model = Model(pre_trained_model.input,x)
    return model

pre_trained_model = InceptionV3(input_shape=(75,75,3),
                                include_top=False,
                                weights='imagenet')

for layer in pre_trained_model.layers:
    layer.trainable = False

last_layer = pre_trained_model.get_layer('mixed5')
last_output = last_layer.output
model = model_output(pre_trained_model,last_output)

model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(
    train_generator,
    epochs =20,
    verbose =1,
    validation_data = val_generator
)

tf.keras.models.save_model(model,'kyp_model.hdf5')

