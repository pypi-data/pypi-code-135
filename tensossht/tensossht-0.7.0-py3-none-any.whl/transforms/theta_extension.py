from pathlib import Path
from typing import Callable, Iterable, Union

import numpy as np
import tensorflow as tf

from tensossht.sampling import ImageAxes, ImageSamplingSchemes

__all__ = ["theta_extension"]
__doc__ = Path(__file__).with_suffix(".rst").read_text()


def theta_extension(
    functions: tf.Tensor,
    axes: ImageAxes,
    is_complex: bool = True,
    spins: Union[int, Iterable[int], tf.Tensor] = 0,
    sampling: Union[str, ImageSamplingSchemes] = ImageSamplingSchemes.MW,
) -> tf.Tensor:
    """Extends a spherical function to 2pi and adds phi weights.

    Args:
        functions: A function where the phi dimension is in Fourier space and the theta
            dimension is in real space.
        axes: axes of the images, theta, phi and (optionally) spin.
        is_complex: If true, the function corresponds to a complex signal.
        spins: If an integer, then the spins will be between `spins` and
            `tf.shape(functions)[spin_dim]`. For a transform over a single spin, `spins
            == spin`. If an iterable or a tensor, then the spins are as given.
        sampling: Whether image-space sampling is MW or MWSS.
    """
    from tensossht.sampling import image_sampling_scheme

    sampling = image_sampling_scheme(sampling)

    axes = axes % len(functions.shape)
    if axes.phi == axes.theta:
        return ValueError("phi and theta must correspond to distinct dimensions")
    if axes.spin is not None and axes.spin == axes.theta:
        return ValueError("spin and theta must correspond to distinct dimensions")
    if axes.spin is not None and axes.spin == axes.phi:
        return ValueError("spin and phi must correspond to distinct dimensions")
    if (
        is_complex
        and sampling == ImageSamplingSchemes.MW
        and 2 * functions.shape[axes.theta] - 1 != functions.shape[axes.phi]
    ):
        msg = "Shape of complex mw image-space signals: phi == 2 * theta - 1"
        raise ValueError(msg)
    elif (
        is_complex
        and sampling == ImageSamplingSchemes.MWSS
        and 2 * functions.shape[axes.theta] - 2 != functions.shape[axes.phi]
    ):
        msg = "Shape of complex mwss image-space signals: phi == 2 * theta - 2"
        raise ValueError(msg)
    elif functions.shape[axes.theta] != functions.shape[axes.phi] and (not is_complex):
        msg = "Shape of real image-space signals: phi == theta"
        raise ValueError(msg)

    is_multi_spin = axes.spin is not None and (
        tf.shape(functions)[axes.spin] is None or tf.shape(functions)[axes.spin] > 1
    )
    impl = factory(is_complex, is_multi_spin, sampling)
    return impl(functions, axes, spins=spins)


def factory(
    is_complex: bool = True,
    is_multi_spin: bool = False,
    sampling: Union[str, ImageSamplingSchemes] = ImageSamplingSchemes.MW,
) -> Callable:
    """Chooses the right theta-extension."""
    from tensossht.sampling import image_sampling_scheme

    sampling = image_sampling_scheme(sampling)

    if is_complex and sampling == ImageSamplingSchemes.MW and is_multi_spin:
        return tf_complex_mw_spin_theta_extension
    elif sampling == ImageSamplingSchemes.MW and is_multi_spin:
        return tf_real_mw_theta_extension
    elif is_complex and is_multi_spin:
        return tf_complex_mwss_spin_theta_extension
    elif is_multi_spin:
        return tf_real_mwss_spin_theta_extension
    elif is_complex and sampling == ImageSamplingSchemes.MW:
        return tf_complex_mw_theta_extension
    elif sampling == ImageSamplingSchemes.MW:
        return tf_real_mw_theta_extension
    elif is_complex:
        return tf_complex_mwss_theta_extension
    return tf_real_mwss_theta_extension


@tf.function
def tf_real_mw_theta_extension(
    functions: tf.Tensor, axes: ImageAxes, **kwargs
) -> tf.Tensor:
    """Tensorflow theta extension function for real mw sampling signals."""
    extension = mw_block(functions, axes.theta)
    factor = real_phi_factor(functions, axes.phi)
    return tf.concat((functions, (factor * extension)), axis=axes.theta)


@tf.function
def tf_complex_mw_theta_extension(
    functions: tf.Tensor, axes: ImageAxes, spins: int = 0
) -> tf.Tensor:
    """Tensorflow theta extension function for complex mw sampling signals."""
    extension = mw_block(functions, axes.theta)
    factor = complex_mw_phi_factor(functions, axes.phi, spin=spins)
    return tf.concat((functions, (factor * extension)), axis=axes.theta)


@tf.function
def tf_real_mwss_theta_extension(
    functions: tf.Tensor, axes: ImageAxes, **kwargs
) -> tf.Tensor:
    """Tensorflow theta extension function for real mwss sampling signals."""
    extension = mwss_block(functions, axes.theta)
    factor = real_phi_factor(functions, axes.phi)
    return tf.concat((functions, (factor * extension)), axis=axes.theta)


@tf.function
def tf_complex_mwss_theta_extension(
    functions: tf.Tensor, axes: ImageAxes, spins: int = 0, **kwargs
) -> tf.Tensor:
    """Tensorflow theta extension function for complex mwss sampling signals."""
    extension = mwss_block(functions, axes.theta)
    factor = complex_mwss_phi_factor(functions, axes.phi, spin=spins)
    return tf.concat((functions, (factor * extension)), axis=axes.theta)


@tf.function
def tf_real_mw_spin_theta_extension(
    functions: tf.Tensor,
    axes: ImageAxes,
    spins: Union[int, Iterable[int], tf.Tensor] = 0,
) -> tf.Tensor:
    """Tensorflow theta extension function for real mw sampling signals."""
    assert axes.spin is not None
    extension = mw_block(functions, axes.theta)
    sfact = spin_factor(functions, axes.spin, spins)
    pfact = real_phi_factor(functions, axes.phi)
    return tf.concat((functions, (sfact * pfact * extension)), axis=axes.theta)


@tf.function
def tf_complex_mw_spin_theta_extension(
    functions: tf.Tensor, axes: ImageAxes, spins: Union[int, Iterable[int], tf.Tensor]
) -> tf.Tensor:
    """Tensorflow theta extension function for complex mw sampling signals."""
    assert axes.spin is not None
    extension = mw_block(functions, axes.theta)
    sfact = spin_factor(functions, axes.spin, spins)
    pfact = complex_mw_phi_factor(functions, axes.phi)
    return tf.concat((functions, (sfact * pfact * extension)), axis=axes.theta)


@tf.function
def tf_real_mwss_spin_theta_extension(
    functions: tf.Tensor, axes: ImageAxes, spins: Union[int, Iterable[int], tf.Tensor]
) -> tf.Tensor:
    """Tensorflow theta extension function for real mwss sampling signals."""
    assert axes.spin is not None
    extension = mwss_block(functions, axes.theta)
    sfact = spin_factor(functions, axes.spin, spins)
    pfact = real_phi_factor(functions, axes.phi)
    return tf.concat((functions, (pfact * sfact * extension)), axis=axes.theta)


@tf.function
def tf_complex_mwss_spin_theta_extension(
    functions: tf.Tensor, axes: ImageAxes, spins: Union[int, Iterable[int], tf.Tensor]
) -> tf.Tensor:
    """Tensorflow theta extension function for complex mwss sampling signals."""
    assert axes.spin is not None
    extension = mwss_block(functions, axes.theta)
    sfact = spin_factor(functions, axes.spin, spins)
    pfact = complex_mwss_phi_factor(functions, axes.phi)
    return tf.concat((functions, (sfact * pfact * extension)), axis=axes.theta)


def mw_block(functions: tf.Tensor, theta_dim: int) -> tf.Tensor:
    ndim = len(functions.shape)
    lmax = functions.shape[theta_dim]
    return tf.reverse(
        tf.slice(
            functions,
            tf.zeros(ndim, dtype=tf.int32),
            tf.one_hot(theta_dim % ndim, ndim, on_value=lmax - 1, off_value=-1),
        ),
        (theta_dim % ndim,),
    )


def mwss_block(functions: tf.Tensor, theta_dim: int) -> tf.Tensor:
    ndim = len(functions.shape)
    lmax = functions.shape[theta_dim] - 1
    return tf.reverse(
        tf.slice(
            functions,
            tf.one_hot(theta_dim % ndim, ndim, on_value=1, off_value=0),
            tf.one_hot(theta_dim % ndim, ndim, on_value=lmax - 1, off_value=-1),
        ),
        (theta_dim % ndim,),
    )


def sign_factor(
    indices: tf.Tensor,
    ndim: int,
    dim: int,
    dtype: Union[np.dtype, tf.DType, str] = tf.complex64,
) -> tf.Tensor:
    one = tf.constant(1, dtype=dtype)
    factor = tf.where(indices % 2 == 0, one, -one)
    factor_shape = tf.one_hot(dim % ndim, ndim, off_value=1, on_value=-1)
    return tf.reshape(factor, factor_shape)


def real_phi_factor(functions: tf.Tensor, phi_dim: int) -> tf.Tensor:
    """Phi factor for MW sampling of real image-space signals."""
    indices = tf.range(functions.shape[phi_dim])
    return sign_factor(indices, len(functions.shape), phi_dim, functions.dtype)


def complex_mw_phi_factor(
    functions: tf.Tensor, phi_dim: int, spin: int = 0
) -> tf.Tensor:
    """Phi factor for MW sampling of complex image-space signals."""
    lmax = (functions.shape[phi_dim] + 1) // 2
    indices = tf.concat((tf.range(lmax), tf.range(-lmax + 1, 0)), 0) + spin
    return sign_factor(indices, len(functions.shape), phi_dim, functions.dtype)


def complex_mwss_phi_factor(
    functions: tf.Tensor, phi_dim: int, spin: int = 0
) -> tf.Tensor:
    """Phi factor for MW sampling of complex image-space signals."""
    lmax = (functions.shape[phi_dim] + 1) // 2
    indices = tf.concat((tf.range(lmax + 1), tf.range(-lmax + 1, 0)), 0) + spin
    return sign_factor(indices, len(functions.shape), phi_dim, functions.dtype)


def spin_factor(
    functions: tf.Tensor, spin_dim: int, spins: Union[int, Iterable[int], tf.Tensor]
) -> tf.Tensor:
    shape = functions.shape
    if isinstance(spins, int):
        spin_range = tf.range(spins, spins + shape[spin_dim])
    elif isinstance(spins, tf.Tensor):
        spin_range = spins
    else:
        spin_range = tf.Tensor(spins)

    return sign_factor(spin_range, len(shape), spin_dim, functions.dtype)
