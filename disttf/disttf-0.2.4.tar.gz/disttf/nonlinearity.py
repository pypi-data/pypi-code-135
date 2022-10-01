import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend as K

import numpy as np


class NonLinearityLayer(keras.layers.Layer):
    def __init__(self, func=None,**kwargs):
        super(NonLinearityLayer, self).__init__(**kwargs)
        if func is None:func=K.abs
        self.func=func

    def build(self, input_shape):
        super(NonLinearityLayer, self).build(input_shape)
        self.delta=self.add_weight(name='delta',shape=input_shape[1:],initializer='zeros',trainable=True)

    def call(self, x):
        #print(x.shape)
        #exit()

        return self.func(x-self.delta)+self.delta

    def compute_output_shape(self, input_shape):
        return input_shape


