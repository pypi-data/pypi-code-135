from typing import Callable, Optional, Union

import numpy as np
import tensorflow as tf

from tensossht.sampling import HarmonicSampling, ImageSamplingBase, ImageSamplingSchemes


class HarmonicTransform:
    """Fast transform between image space and spherical harmonic space."""

    def __init__(
        self,
        forward: Callable,
        inverse: Callable,
        image_sampling: ImageSamplingBase,
        harmonic_sampling: HarmonicSampling,
    ):
        self.forward = forward
        self.inverse = inverse
        self.sampling = image_sampling
        """Image-space sampling"""
        self.harmonic_sampling = harmonic_sampling
        """Harmonic-space sampling"""

    @property
    def lmax(self):
        return self.harmonic_sampling.lmax

    @property
    def lmin(self):
        return self.harmonic_sampling.lmin

    @property
    def mmax(self):
        return self.harmonic_sampling.mmax

    @property
    def mmin(self):
        return self.harmonic_sampling.mmin

    @property
    def smax(self):
        return self.harmonic_sampling.smax

    @property
    def smin(self):
        return self.harmonic_sampling.smin

    @property
    def labels(self):
        return self.harmonic_sampling.labels

    @property
    def llabels(self):
        return self.harmonic_sampling.labels[0]

    @property
    def mlabels(self):
        return self.harmonic_sampling.labels[1]

    @property
    def slabels(self):
        return self.harmonic_sampling.labels[2]

    @property
    def ncoeffs(self):
        return self.harmonic_sampling.labels.shape[1]

    @property
    def thetas(self):
        return self.sampling.thetas

    @property
    def phis(self):
        return self.sampling.phis

    @property
    def grid(self):
        return self.sampling.grid

    @property
    def points(self):
        """Image-space points."""
        return tf.transpose(tf.reshape(self.grid, (2, -1)))

    @property
    def real_dtype(self):
        if self.sampling.dtype == tf.complex64:
            return tf.float32
        if self.sampling.dtype == tf.complex128:
            return tf.float64
        return self.sampling.dtype

    @property
    def complex_dtype(self):
        if self.sampling.dtype == tf.float32:
            return tf.complex64
        if self.sampling.dtype == tf.float64:
            return tf.complex128
        return self.sampling.dtype

    @property
    def real(self):
        """Transform for real signals.

        If the transform is already for real signals (:math:`m_\\mathrm{min} \\geq 0`),
        then this property returns self. Otherwise it returns an equivalent transform
        with :math:`m_\\mathrm{min} = 0`.
        """
        from tensossht.sampling import image_sampling_scheme

        if self.mmin >= 0:
            return self
        if self.mmax < 0:
            msg = f"Weird mmax={self.mmax}. Cannot infer transform for real signals."
            raise RuntimeError(msg)
        return harmonic_transform(
            lmax=self.lmax,
            lmin=self.lmin,
            mmin=0,
            mmax=self.mmax,
            smax=self.smax,
            smin=self.smin,
            dtype=self.real_dtype,
            sampling=image_sampling_scheme(self.sampling.__class__.__name__),
        )

    @property
    def complex(self):
        """Transform for complex signals.

        If the transform is already for complex signals
        (:math:`m_\\mathrm{min} \\leq 0`), then this property returns self. Otherwise it
        returns an equivalent transform with :math:`m_\\mathrm{min} = -l_\\mathrm{max}`.
        """
        from tensossht.sampling import image_sampling_scheme

        if self.mmin <= 0:
            return self
        return harmonic_transform(
            lmax=self.lmax,
            lmin=self.lmin,
            mmin=-self.lmax,
            mmax=self.mmax,
            smax=self.smax,
            smin=self.smin,
            dtype=self.complex_dtype,
            sampling=image_sampling_scheme(self.sampling.__class__.__name__),
        )


def harmonic_transform(
    lmax: Optional[int] = None,
    lmin: Optional[int] = 0,
    mmax: Optional[int] = None,
    mmin: Optional[int] = None,
    smax: Optional[int] = None,
    smin: Optional[int] = None,
    spin: Optional[int] = None,
    sampling: Union[str, ImageSamplingSchemes] = ImageSamplingSchemes.MW,
    dtype: Union[str, np.dtype, tf.DType] = tf.float32,
) -> HarmonicTransform:
    """Creates a harmonic transform.

    Args:
        lmax: Maximum degree. If None or absent, labels should be given.
        lmin: Minimum degree, defaults to zero. Ignored if lmax is absent.
        mmax: Maximum order. If None, defaults to ``lmax``. Ignored if lmax is absent.
        mmin: Minimum order. If None, defaults to ``-lmax``. For real image-space
            signals, use ``mmin=0``. Ignored if lmax is absent.
        labels: 2-d tensor with the l and  m labels. Alternative to lmax and friends. If
            absent or None, lmax should be given.
        sampling: image-space sampling scheme. Can be a string, e.g. "MW", or one of
            :py:enum:`~tensossht.sampling.ImageSamplingSchemes`.
        dtype: Underlying floating point type.
    """
    from tensossht.sampling import harmonic_sampling_scheme, image_sampling_scheme
    from tensossht.transforms.forward import forward_transform
    from tensossht.transforms.inverse import inverse_transform

    hsampling = harmonic_sampling_scheme(
        lmax=lmax,
        lmin=lmin,
        mmax=mmax,
        mmin=mmin,
        smin=smin,
        smax=smax,
        spin=spin,
        compact_spin=False,
    )
    isampling = image_sampling_scheme(sampling).value(hsampling.lmax, dtype)
    forward = forward_transform(hsampling, dtype=dtype, sampling=sampling)
    inverse = inverse_transform(hsampling, dtype=dtype, sampling=sampling)
    return HarmonicTransform(forward, inverse, isampling, hsampling)
