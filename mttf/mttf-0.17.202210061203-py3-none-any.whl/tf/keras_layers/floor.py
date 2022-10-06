import tensorflow as tf


__all__ = ["Floor"]


@tf.custom_gradient
def floor(x, size: float = 1.0):
    if size == 1.0:
        x = tf.math.floor(x)
    else:
        x /= size
        x = tf.math.floor(x)
        x *= size
    def grad(upstream): # identity
        return upstream
    return x, grad


class Floor(tf.keras.layers.Layer):
    """TensorFlow floor with optional size but gradient is identity."""

    def __init__(self, size: float = 1.0, **kwargs):
        self._size = size
        super().__init__(**kwargs)

    def call(self, x):
        return floor(x, self._size)

    call.__doc__ = tf.keras.layers.Layer.call.__doc__

    def compute_output_shape(self, input_shape):
        return input_shape

    compute_output_shape.__doc__ = tf.keras.layers.Layer.compute_output_shape.__doc__

    def get_config(self):
        config = {
            "size": self._size,
        }
        base_config = super(Floor, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

    get_config.__doc__ = tf.keras.layers.Layer.get_config.__doc__

