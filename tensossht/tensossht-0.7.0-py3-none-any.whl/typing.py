from typing import Union

import numpy as np
import tensorflow as tf

TFArray = np.ndarray
Array = Union[np.ndarray, TFArray]
ArrayVar = Union[np.ndarray, TFArray, tf.Variable]
TensorShape = tf.TensorShape
