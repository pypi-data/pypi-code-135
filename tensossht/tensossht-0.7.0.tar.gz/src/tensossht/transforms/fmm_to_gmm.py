from typing import Union

import numpy as np
import tensorflow as tf

from tensossht.references import REFERENCES


class ComplexFmmToGmm:
    f"""Convolves Fmm with weighs.

    See [McEwen, Wiaux (2011)], equation 19.

    {REFERENCES['MW']}
    """

    def __init__(self, lmax: int, dtype: Union[np.dtype, tf.DType, str] = tf.float32):
        cdtype = {tf.float64: tf.complex128, tf.float32: tf.complex64}.get(dtype, dtype)
        self.weights = tf.signal.fft(
            tf.signal.ifftshift(tf.constant(weights(lmax), dtype=cdtype))
        )

    @tf.function
    def __call__(self, fmm: tf.Tensor) -> tf.Tensor:
        return convolve(fmm, self.weights)


class RealFmmToGmm(ComplexFmmToGmm):
    @tf.function
    def __call__(self, fmm: tf.Tensor) -> tf.Tensor:
        """Add negative mp to result.

        Expects that phi is the second to last coordinate.
        """
        gmm = super().__call__(fmm)
        return tf.concat((gmm[..., -1:0:-1, :], gmm), axis=-2)


def fmm_to_gmm(
    lmax: int,
    dtype: Union[np.dtype, tf.DType, str] = tf.float32,
    is_real: bool = False,
) -> ComplexFmmToGmm:
    """Factory function for fmm to gmm operation."""
    dtype = tf.dtypes.as_dtype(dtype)
    return (RealFmmToGmm if is_real else ComplexFmmToGmm)(lmax, dtype)


def convolve(fmm: tf.Tensor, weights: tf.Tensor) -> tf.Tensor:
    """Convolve Fmm and weights.

    Assumes that ``Fmm[..., 0]`` corrsponds to ``-2 * (L - 1)``.
    Assumes that ``weights`` has already been converted to Fourier space (see
    :py:meth:`HarmonicTransform.__init__`).
    """
    lm1 = (fmm.shape[-1] + 1) // 2 - 1
    padded = tf.pad(
        fmm,
        tf.concat(
            (
                tf.zeros((len(fmm.shape) - 1, 2), dtype=tf.int32),
                tf.fill((1, 2), tf.cast(lm1, dtype=tf.int32)),
            ),
            axis=0,
        ),
    )
    convolved = tf.signal.ifft(tf.signal.fft(padded) * weights)
    return convolved[..., lm1 : (fmm.shape[-1] + lm1)]


def weights(L: int, dtype=complex) -> np.ndarray:
    r"""Array of weights.

    .. code:: math

        w(+1) = i\frac{\pi}{2]}

        w(-1) = -i\frac{\pi}{2]}

        w(2m) = \frac{2}{1 - m^2}

        w(2m + 1) = 0
    """

    def weight(m: int) -> complex:
        if abs(m) == 1:
            return -np.sign(m) * np.pi / 2 * 1j
        elif m % 2 == 0:
            return 2 / (1 - m * m)
        return 0

    return np.fromiter((weight(m) for m in range(-2 * L + 2, 2 * L - 1)), dtype=dtype)
