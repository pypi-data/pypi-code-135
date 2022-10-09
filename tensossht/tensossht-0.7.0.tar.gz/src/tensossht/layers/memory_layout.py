from pathlib import Path
from typing import Union

import numpy as np
import tensorflow as tf

__doc__ = Path(__file__).with_suffix(".rst").read_text()


class PackingLayer(tf.keras.layers.Layer):
    """Packs coefficients from (l, m) matrix to memory efficient format."""

    def __init__(
        self,
        is_real: bool = False,
        coeff_dim: int = -1,
        l_dim: int = -2,
        m_dim: int = -1,
        **kwargs,
    ):
        if kwargs.pop("trainable", False):
            raise ValueError("This layer is not trainable")
        super().__init__(trainable=False, **kwargs)
        self.is_real = is_real
        self.coeff_dim = coeff_dim
        self.l_dim = l_dim
        self.m_dim = m_dim
        self.labels = tf.zeros((2, 0), dtype=tf.int32)

    def __call__(self, tensor: tf.Tensor) -> tf.Tensor:
        return super().__call__(tensor)

    def build(self, shape: tf.TensorShape):
        from tensossht.sampling import legendre_labels

        lmax = shape[self.l_dim]
        mmin = 0 if self.is_real else 1 - lmax
        self.labels = legendre_labels(lmax=lmax, mmin=mmin)

    def call(self, inputs) -> tf.Tensor:
        """Call layer."""
        from tensossht.specialfunctions import to_compressed_coefficients

        return to_compressed_coefficients(  # type: ignore
            inputs,
            labels=self.labels,
            l_dim=self.l_dim,
            m_dim=self.m_dim,
            coeff_dim=self.coeff_dim,
        )

    def get_config(self):
        config = super().get_config()
        config.update(
            dict(
                is_real=self.is_real,
                l_dim=self.l_dim,
                m_dim=self.m_dim,
                coeff_dim=self.coeff_dim,
            )
        )
        return config


class UnpackingLayer(tf.keras.layers.Layer):
    """Unpacks coefficients to a 2-matrix (l, m)."""

    def __init__(
        self,
        is_real: bool = False,
        coeff_dim: int = -1,
        l_dim: int = -2,
        m_dim: int = -1,
        fill_value: Union[int, float, complex] = 0,
        **kwargs,
    ):
        if kwargs.pop("trainable", False):
            raise ValueError("This layer is not trainable")
        super().__init__(trainable=False, **kwargs)
        self.is_real = is_real
        self.coeff_dim = coeff_dim
        self.l_dim = l_dim
        self.m_dim = m_dim
        self.fill_value = fill_value
        self.lmax = tf.zeros((), dtype=tf.int32)

    def __call__(self, tensor: tf.Tensor) -> tf.Tensor:
        return super().__call__(tensor)

    def build(self, shape: tf.TensorShape):
        if not self.is_real:
            self.lmax = int(np.sqrt(shape[self.coeff_dim]))
            assert self.lmax * self.lmax == shape[self.coeff_dim]
        else:
            self.lmax = int(np.sqrt(1 + 8 * shape[self.coeff_dim]) - 1) // 2
            assert self.lmax * (self.lmax + 1) == 2 * shape[self.coeff_dim]

    def call(self, inputs) -> tf.Tensor:
        """Call layer."""
        from tensossht.specialfunctions import to_matrix_coefficients

        mmin = 0 if self.is_real else None

        return to_matrix_coefficients(  # type: ignore
            inputs,
            lmax=self.lmax,
            mmin=mmin,
            l_dim=self.l_dim,
            m_dim=self.m_dim,
            coeff_dim=self.coeff_dim,
            fill_value=self.fill_value,
        )

    def get_config(self):
        config = super().get_config()
        config.update(
            dict(
                is_real=self.is_real,
                coeff_dim=self.coeff_dim,
                l_dim=self.l_dim,
                m_dim=self.m_dim,
                fill_value=self.fill_value,
            )
        )
        return config
