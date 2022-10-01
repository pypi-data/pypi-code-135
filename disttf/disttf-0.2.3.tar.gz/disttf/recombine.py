import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend as K

import numpy as np


class RecombineLayer(keras.layers.Layer):
    def __init__(self,**kwargs):
        super(RecombineLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        super(RecombineLayer, self).build(input_shape)

    def call(self, x):
        (a1,b1),(a2,b2)=x
        a=K.concatenate([a1,a2],axis=1)
        b=K.concatenate([b1,b2],axis=0)
        return (a,b)

    def compute_output_shape(self, input_shape):
        (a1,b1),(a2,b2)=input_shape
        return (a1[0],a1[1]+a2[1],a1[2]),(b1[0]+b2[0])

