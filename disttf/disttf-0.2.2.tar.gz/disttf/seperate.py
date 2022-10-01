import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend as K

import numpy as np


class SeperateLayer(keras.layers.Layer):
    def __init__(self, cut=1,**kwargs):
        super(SeperateLayer, self).__init__(**kwargs)
        self.cut = cut

    def build(self, input_shape):
        super(SeperateLayer, self).build(input_shape)

    def call(self, x):
        a,b=x
        a1=a[:,:self.cut]
        a2=a[:,self.cut:]
        b1=b[:self.cut]
        b2=b[self.cut:]
        return (a1,b1),(a2,b2)

    def compute_output_shape(self, input_shape):
        a,b=input_shape
        a1=[a[0],self.cut,a[2]]
        a2=[a[0],a[1]-self.cut,a[2]]
        b1=[self.cut]
        b2=[b[0]-self.cut]
        return (a1,b1),(a2,b2)


