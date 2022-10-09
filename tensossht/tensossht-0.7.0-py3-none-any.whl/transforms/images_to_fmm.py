from typing import Callable, Optional, Tuple, Union

import numpy as np
import tensorflow as tf

from tensossht.references import REFERENCES
from tensossht.sampling import Axis, HarmonicSampling, ImageAxes, ImageSamplingSchemes


class ImagesToFmm:
    f"""Fmm from [McEwen, Wiaux (2011)] part IV.D.

    ${REFERENCES['MW']}
    """

    def __init__(
        self,
        phi_fft: Callable,
        theta_extension: Callable,
        shift: Callable,
        remove_offset: Callable,
        error_checking: Optional[Callable] = None,
    ):
        self.phi_fft = phi_fft
        self.theta_extension = theta_extension
        self.shift = shift
        self.remove_offset = remove_offset
        self.error_checking = error_checking

    @tf.function
    def __call__(self, images: tf.Tensor, axes: ImageAxes) -> tf.Tensor:
        if self.error_checking:
            self.error_checking(images, axes)
        normalization_factor = images.shape[axes.phi]
        functionsT, axes = reorder_for_fft(images, axes, Axis.PHI)
        f_theta_m = self.phi_fft(functionsT)
        f_2theta_m = self.theta_extension(f_theta_m, axes)
        f_2theta_mT, axes = reorder_for_fft(f_2theta_m, axes, Axis.THETA)
        fmm = tf.signal.fft(f_2theta_mT) / normalization_factor**2
        return self.remove_offset(self.shift(fmm))


def images_to_fmm(
    hsampling: Union[HarmonicSampling, int, tf.Tensor],
    sampling: Union[str, ImageSamplingSchemes] = ImageSamplingSchemes.MW,
    dtype: Union[np.dtype, tf.DType, str] = tf.float32,
) -> ImagesToFmm:
    from functools import partial

    from tensossht.sampling import harmonic_sampling_scheme, image_sampling_scheme
    from tensossht.transforms.theta_extension import factory

    dtype = tf.dtypes.as_dtype(dtype)
    sampling = image_sampling_scheme(sampling)
    hsampling = harmonic_sampling_scheme(hsampling)

    if hsampling.is_multi_spin and not hsampling.is_separable_spin:
        raise NotImplementedError("Cannot work with non-separable spins")
    theta_extension = partial(
        factory(hsampling.is_complex, hsampling.is_multi_spin, sampling),
        spins=hsampling.spins,
    )
    if hsampling.is_real and sampling == ImageSamplingSchemes.MW:
        return ImagesToFmm(
            phi_fft=tf.signal.rfft,
            theta_extension=theta_extension,
            shift=real_shift,
            remove_offset=partial(
                tf.math.multiply, mw_modulation(hsampling.lmax, dtype)
            ),
            error_checking=partial(real_mw_checks, hsampling.lmax),
        )
    elif sampling == ImageSamplingSchemes.MW:
        return ImagesToFmm(
            phi_fft=tf.signal.fft,
            theta_extension=theta_extension,
            shift=complex_shift,
            remove_offset=partial(
                tf.math.multiply, mw_modulation(hsampling.lmax, dtype)
            ),
            error_checking=partial(complex_mw_checks, hsampling.lmax),
        )
    elif hsampling.is_real:
        return ImagesToFmm(
            phi_fft=tf.signal.rfft,
            theta_extension=theta_extension,
            shift=real_shift,
            remove_offset=real_mwss_offset,
            error_checking=partial(real_mwss_checks, hsampling.lmax),
        )
    else:
        return ImagesToFmm(
            phi_fft=tf.signal.fft,
            theta_extension=theta_extension,
            shift=complex_shift,
            remove_offset=complex_mwss_offset,
            error_checking=partial(complex_mwss_checks, hsampling.lmax),
        )


def reorder_for_fft(
    functions: tf.Tensor, axes: ImageAxes, *shifted_axes: Union[str, Axis]
) -> Tuple[tf.Tensor, ImageAxes]:
    """Reorder functor so that the shifted axes are last."""
    return (
        axes.transpose(functions, *shifted_axes),
        axes.shift(len(functions.shape), *shifted_axes),
    )


def mw_modulation(
    lmax: int, dtype: Union[np.dtype, tf.DType, str] = tf.float32
) -> tf.Tensor:
    rdtype = tf.dtypes.as_dtype(dtype).real_dtype
    return tf.exp(
        tf.complex(
            tf.constant(0, dtype=rdtype),
            tf.constant(-np.pi / (2 * lmax - 1), rdtype)
            * tf.range(-(lmax - 1), lmax, dtype=rdtype),
        )
    )


@tf.function
def real_mwss_offset(data: tf.Tensor) -> tf.Tensor:
    """Removes extra data resulting from MWSS sampling."""
    return data[..., :-1, 1:]


@tf.function
def complex_mwss_offset(data: tf.Tensor) -> tf.Tensor:
    """Removes extra data resulting from MWSS sampling."""
    return data[..., 1:, 1:]


@tf.function
def real_shift(fmm: tf.Tensor) -> tf.Tensor:
    return tf.signal.fftshift(fmm, len(fmm.shape) - 1)


@tf.function
def complex_shift(fmm: tf.Tensor) -> tf.Tensor:
    ndim = len(fmm.shape)
    return tf.signal.fftshift(fmm, (ndim - 2, ndim - 1))


def real_mw_checks(lmax: int, images: tf.Tensor, axes: ImageAxes):
    axes = axes % len(images.shape)

    if axes.phi == axes.theta:
        raise ValueError("Theta and phi dimensions are the same")
    if images.dtype != tf.float64 and images.dtype != tf.float32:
        raise ValueError("Real space signal is not real")
    if images.shape[axes.phi] != 2 * lmax - 1:
        x = images.shape[axes.phi]
        msg = f"The size of the phi dimension ought to be {2 * lmax - 1}, not {x}"
        raise ValueError(msg)
    if images.shape[axes.theta] != lmax:
        x = images.shape[axes.theta]
        msg = f"The size of the theta dimension ought to be {lmax}, not {x}"
        raise ValueError(msg)


def real_mwss_checks(lmax: int, images: tf.Tensor, axes: ImageAxes):
    axes = axes % len(images.shape)

    if axes.phi == axes.theta:
        raise ValueError("Theta and phi dimensions are the same")
    if images.dtype != tf.float64 and images.dtype != tf.float32:
        raise ValueError("Real space signal is not real")
    if images.shape[axes.phi] != 2 * lmax:
        x = images.shape[axes.phi]
        msg = f"The size of the phi dimension ought to be {2 * lmax}, not {x}"
        raise ValueError(msg)
    if images.shape[axes.theta] != lmax + 1:
        x = images.shape[axes.theta]
        msg = f"The size of the theta dimension ought to be {lmax + 1}, not {x}"
        raise ValueError(msg)


def complex_mw_checks(lmax: int, images: tf.Tensor, axes: ImageAxes):
    axes = axes % len(images.shape)

    if axes.phi == axes.theta:
        raise ValueError("Theta and phi dimensions are the same")
    if images.dtype != tf.complex64 and images.dtype != tf.complex128:
        raise ValueError("Real space signal is not complex")
    if images.shape[axes.phi] != 2 * lmax - 1:
        x = images.shape[axes.phi]
        msg = f"The size of the phi dimension ought to be {2 * lmax - 1}, not {x}"
        raise ValueError(msg)
    if images.shape[axes.theta] != lmax:
        x = images.shape[axes.theta]
        msg = f"The size of the theta dimension ought to be {lmax}, not {x}"
        raise ValueError(msg)


def complex_mwss_checks(lmax: int, images: tf.Tensor, axes: ImageAxes):
    axes = axes % len(images.shape)

    if axes.phi == axes.theta:
        raise ValueError("Theta and phi dimensions are the same")
    if images.dtype != tf.complex64 and images.dtype != tf.complex128:
        raise ValueError("Real space signal is not complex")
    if images.shape[axes.phi] != 2 * lmax:
        x = images.shape[axes.phi]
        msg = f"The size of the phi dimension ought to be {2 * lmax}, not {x}"
        raise ValueError(msg)
    if images.shape[axes.theta] != lmax + 1:
        x = images.shape[axes.theta]
        msg = f"The size of the theta dimension ought to be {lmax + 1}, not {x}"
        raise ValueError(msg)
