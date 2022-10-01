import numpy as np

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend as K

#from tensorflow.contrib.distributions import fill_triangular
#from tensorflow.distributions.utils import fill_triangular
from tensorflow_probability import math
fill_triangular=math.fill_triangular

class MixtureLayer(keras.layers.Layer):
    def __init__(self, **kwargs):
        super(MixtureLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        dim=input_shape[-1].value
        count=dim*(dim+1)//2
        modes=input_shape[-2]
        self.M1 = self.add_weight(name='M', shape=(modes,count,), initializer='uniform', trainable=True)
        self.M2 = self.add_weight(name='M', shape=(modes,count,), initializer='uniform', trainable=True)
        self.built = True

    #return self.M, but with the lower triangle set to zero
    def remove_diag(self,mat, input_shape):
        dim=input_shape[-1]
        def subfunc(x):
            return tf.linalg.set_diag(x, tf.ones(dim))
        return tf.map_fn(subfunc,mat)

    def mat1(self, input_shape):
        ret=fill_triangular(self.M1)
        return self.remove_diag(ret,input_shape)#tf.linalg.set_diag(ret, tf.ones(input_shape[-1]))
    #like mat2, but with the upper triangle set to zero
    def mat2(self, input_shape):
        ret=fill_triangular(self.M2, upper=True)
        return self.remove_diag(ret,input_shape)#tf.linalg.set_diag(ret, tf.ones(input_shape[-1]))


 
    def compute_output_shape(self, input_shape):
        return input_shape

    def call(self, inputs, mask=None):
        m1=self.mat1(inputs.shape)
        m2=self.mat2(inputs.shape)

        def subfunc(x):
            return K.batch_dot(K.batch_dot(x,m1),m2)
            return tf.matmul(x,m1)


        #print(m1.shape)
        #print(m2.shape)
        #print(inputs.shape)
        #print(K.dot(inputs,m1).shape)
        #print(K.batch_dot(inputs,m1,axes=(2,1)).shape)
        ret=tf.map_fn(subfunc,inputs)
        #print(ret.shape)
        #exit()
        return ret
        #return K.dot(K.dot(inputs, m1), m2)

    def get_config(self):
        config = super(MixtureLayer, self).get_config()
        return config




