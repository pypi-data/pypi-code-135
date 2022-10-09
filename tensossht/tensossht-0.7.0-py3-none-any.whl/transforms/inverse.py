from typing import Callable, Optional, Type, Union, cast

import numpy as np
import tensorflow as tf

from tensossht.references import REFERENCES
from tensossht.sampling import (
    HarmonicAxes,
    HarmonicSampling,
    ImageAxes,
    ImageSamplingSchemes,
)
from tensossht.typing import TFArray


class InverseTransformBase:
    f"""Inverse Spherical Harmonic Transform.

    Converts harmonic space  signals to image space signals, following [McEwen, Wiaux
    (2011)], section IV.D.

    {REFERENCES['MW']}
    """

    def __init__(
        self,
        coeffs_to_fmm: Callable[[TFArray, HarmonicAxes], TFArray],
        fft: Callable[[TFArray], TFArray],
        slicer: Callable[[TFArray], TFArray],
    ):
        self.coeffs_to_fmm = coeffs_to_fmm
        self.fft = fft
        self.slicer = slicer

    def _call(
        self, coefficients: TFArray, in_axes: HarmonicAxes, out_axes: ImageAxes
    ) -> TFArray:
        fmm = self.coeffs_to_fmm(coefficients, in_axes)
        overspectral = self.fft(fmm)
        hspace = self.slicer(overspectral)
        return ImageAxes(
            theta=-2, phi=-1, spin=None if in_axes.spin is None else -3
        ).transpose(hspace, out_axes)


class InverseTransform(InverseTransformBase):
    f"""Inverse Spherical Harmonic Transform.

    Converts harmonic space  signals to image space signals, following [McEwen, Wiaux
    (2011)], section IV.D.

    {REFERENCES['MW']}
    """

    @tf.function
    def __call__(
        self,
        coefficients: TFArray,
        theta_dim: int = -2,
        phi_dim: int = -1,
        coeff_dim: int = -1,
    ) -> TFArray:
        return self._call(
            coefficients,
            HarmonicAxes(coeff=coeff_dim),
            ImageAxes(theta=theta_dim, phi=phi_dim),
        )


class InverseSpinTransform(InverseTransformBase):
    f"""Inverse Spherical Spin Harmonic Transform.

    Converts harmonic space  signals to image space signals, following [McEwen, Wiaux
    (2011)], section IV.D.

    {REFERENCES['MW']}
    """

    @tf.function
    def __call__(
        self,
        coefficients: TFArray,
        spin_dim: int = -2,
        coeff_dim: int = -1,
        out_spin_dim: int = -3,
        theta_dim: int = -2,
        phi_dim: int = -1,
    ) -> TFArray:
        return self._call(
            coefficients,
            HarmonicAxes(coeff=coeff_dim, spin=spin_dim),
            ImageAxes(theta=theta_dim, phi=phi_dim, spin=out_spin_dim),
        )


def inverse_transform(
    lmax: Optional[Union[int, HarmonicSampling, TFArray]] = None,
    lmin: Optional[int] = None,
    mmax: Optional[int] = None,
    mmin: Optional[int] = None,
    smin: Optional[int] = None,
    smax: Optional[int] = None,
    spin: Optional[int] = None,
    compact_spin: Optional[bool] = None,
    labels: Optional[TFArray] = None,
    dtype: Union[str, np.dtype, tf.DType] = tf.float32,
    sampling: Union[str, ImageSamplingSchemes] = ImageSamplingSchemes.MW,
) -> Union[InverseTransform, InverseSpinTransform]:
    """Factory function for the forward transform."""
    from tensossht.sampling import harmonic_sampling_scheme, image_sampling_scheme
    from tensossht.transforms.coeffs_to_fmm import coeffs_to_fmm

    hsampling = harmonic_sampling_scheme(
        lmax=lmax,
        lmin=lmin,
        mmax=mmax,
        mmin=mmin,
        smin=smin,
        smax=smax,
        spin=spin,
        labels=labels,
        compact_spin=compact_spin,
    )
    sampling = image_sampling_scheme(sampling)
    rdtype = tf.dtypes.as_dtype(dtype).real_dtype

    if hsampling.is_multi_spin and hsampling.is_separable_spin:
        Transform: Union[
            Type[InverseSpinTransform], Type[InverseTransform]
        ] = InverseSpinTransform
    elif not hsampling.is_multi_spin:
        Transform = InverseTransform
    else:
        raise NotImplementedError("Non-separable multi-spin transform not implemented")

    ctof = cast(
        Callable[[TFArray, HarmonicAxes], TFArray],
        coeffs_to_fmm(hsampling, sampling, rdtype),
    )
    fft = inverse_fft_factory(hsampling, sampling, rdtype)
    slicer = inverse_slicer_factory(hsampling, sampling)
    return Transform(coeffs_to_fmm=ctof, fft=fft, slicer=slicer)


def inverse_fft_factory(
    hsampling: HarmonicSampling,
    sampling: ImageSamplingSchemes,
    dtype: tf.DType = tf.float32,
) -> Callable[[TFArray], TFArray]:
    if hsampling.is_real:

        def real_fft(signal: TFArray) -> TFArray:
            length = (
                cast(ImageSamplingSchemes, sampling)
                .value(hsampling.lmax, dtype)
                .shape[1]
            )
            return tf.signal.irfft2d(signal, fft_length=tf.fill((2,), length))

        result: Callable[[TFArray], TFArray] = real_fft
    else:

        def complex_fft(signal: TFArray) -> TFArray:
            ndim = len(signal.shape)
            return cast(
                TFArray, tf.signal.ifft2d(tf.signal.ifftshift(signal, axes=ndim - 1))
            )

        result = complex_fft

    return result


def inverse_slicer_factory(
    hsampling: HarmonicSampling, sampling: ImageSamplingSchemes
) -> Callable[[TFArray], TFArray]:
    if sampling == ImageSamplingSchemes.MW:
        end = hsampling.lmax
    else:
        end = hsampling.lmax + 1

    def slicer(signal: TFArray) -> TFArray:
        return signal[..., :end, :]

    return slicer
