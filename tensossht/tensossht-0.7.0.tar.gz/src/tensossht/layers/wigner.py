from pathlib import Path
from typing import Callable, Optional, Sequence, Union, cast

import numpy as np
import tensorflow as tf

from tensossht.layers.harmonic_transforms import ForwardSpinLayer, InverseSpinLayer
from tensossht.sampling import HarmonicAxes, HarmonicSampling, ImageSamplingSchemes

__doc__ = Path(__file__).with_suffix(".rst").read_text()


class FourierLayer(tf.keras.layers.Layer):
    """Performs a Fourier transform.

    Performs a forward or inverse Fourier transform. The axis is moved back to the
    ``out_axis`` position, defaulting to last position to avoid unnecessary transforms.
    """

    def __init__(
        self,
        is_forward: bool = True,
        is_real: bool = False,
        axis: int = -1,
        out_axis: int = -1,
        is_odd_spin: Optional[bool] = None,
        **kwargs,
    ):
        if kwargs.pop("trainable", False):
            raise ValueError("This layer is not trainable")
        super().__init__(trainable=False, **kwargs)
        self.is_forward = is_forward
        self.axis = axis
        self.out_axis = out_axis
        self.is_real = is_real
        self.is_odd_spin = is_odd_spin

        self._input_perm: Callable[[tf.Tensor], tf.Tensor] = self._build_not_called
        self._output_perm: Callable[[tf.Tensor], tf.Tensor] = self._build_not_called
        self._transform: Callable[[tf.Tensor], tf.Tensor] = self._build_not_called

    def __call__(self, tensor: tf.Tensor) -> tf.Tensor:
        return super().__call__(tensor)

    def build(self, input_shape: tf.TensorShape):
        from functools import partial

        super().build(input_shape)

        def permutation(axis, shape):
            from functools import partial

            axis %= len(shape)
            permutation = [i for i in range(len(shape)) if i != axis]
            permutation.append(axis)
            if axis == len(shape) - 1:
                return lambda x: x
            else:
                return partial(tf.transpose, perm=permutation)

        self._input_perm = permutation(self.axis, input_shape)
        self._output_perm = permutation(self.out_axis, input_shape)
        if self.is_real and self.is_forward:
            self._transform = cast(Callable[[tf.Tensor], tf.Tensor], tf.signal.rfft)
        elif self.is_real and self.is_odd_spin:
            fft_length = tf.constant((2 * input_shape[self.axis] - 1,), dtype=tf.int32)
            self._transform = partial(tf.signal.irfft, fft_length=fft_length)
        elif self.is_real:
            self._transform = cast(Callable[[tf.Tensor], tf.Tensor], tf.signal.irfft)
        elif self.is_forward:
            self._transform = cast(Callable[[tf.Tensor], tf.Tensor], tf.signal.fft)
        else:
            self._transform = cast(Callable[[tf.Tensor], tf.Tensor], tf.signal.ifft)

    @tf.function
    def call(self, inputs) -> tf.Tensor:
        permuted = self._input_perm(inputs)
        transformed = self._transform(permuted)
        return self._output_perm(transformed)

    def get_config(self):
        config = super().get_config()
        config.update(
            dict(
                is_forward=self.is_forward,
                is_real=self.is_real,
                axis=self.axis,
                is_odd_spin=self.is_odd_spin,
            )
        )
        return config

    def compute_output_shape(self, input_shape: tf.TensorShape) -> tf.TensorShape:
        if not self.is_real:
            nspins = input_shape[self.axis]
        elif self.is_forward:
            nspins = input_shape[self.axis] // 2 + 1
        elif self.is_odd_spin:
            nspins = 2 * input_shape[self.axis] - 1
        else:
            nspins = 2 * input_shape[self.axis] - 2
        result = list(input_shape)
        result.pop(self.axis)
        result.insert(self.out_axis % len(input_shape), nspins)
        return tf.TensorShape(result)

    @staticmethod
    def _build_not_called(_: tf.Tensor) -> tf.Tensor:
        raise RuntimeError("Build was not called")


class ForwardWignerLayer(tf.keras.layers.Layer):
    """Performs a forward Wigner transform."""

    def __init__(
        self,
        fourier_transform: FourierLayer,
        harmonic_transform: ForwardSpinLayer,
        **kwargs,
    ):

        if kwargs.pop("trainable", False):
            raise ValueError("This layer is not trainable")
        super().__init__(trainable=False, **kwargs)

        self._fourier = fourier_transform
        self._harmonic = harmonic_transform
        self._spin_offset = tf.constant(0)
        self._lfactor = tf.constant(0)

    def build(self, input_shape):
        from tensossht.sampling import Axis, HarmonicAxes, ImageAxes

        super().build(input_shape)

        assert isinstance(self._harmonic.in_axes, ImageAxes)
        self._harmonic.in_axes = self._harmonic.in_axes.shift(
            len(input_shape), Axis.SPIN
        )
        self._fourier.build(input_shape)
        if input_shape is None:
            raise ValueError()
        shape = self._fourier.compute_output_shape(input_shape)
        self._harmonic.build(shape)
        hsampling = self._harmonic.harmonic_sampling(shape)
        rdtype = tf.dtypes.as_dtype(self.dtype).real_dtype
        cdtype = tf.complex(tf.zeros(0, dtype=rdtype), tf.zeros(0, dtype=rdtype)).dtype
        self._lfactor = (
            _lfactor(
                hsampling=hsampling,
                axes=cast(HarmonicAxes, self._harmonic.out_axes),
                input_shape=input_shape,
                dtype=cdtype,
            )
            * _sfactor(
                hsampling=hsampling,
                axes=cast(HarmonicAxes, self._harmonic.out_axes),
                input_shape=input_shape,
                dtype=cdtype,
            )
            / input_shape[self._fourier.axis]
        )

    @tf.function
    def call(self, inputs: tf.Tensor) -> tf.Tensor:
        gamma_fourier = self._fourier(inputs)
        if not self._fourier.is_real:
            gamma_fourier = tf.signal.fftshift(gamma_fourier, self._fourier.out_axis)
        return cast(Callable, self._harmonic)(gamma_fourier) * self._lfactor


class InverseWignerLayer(tf.keras.layers.Layer):
    """Performs an inverse Wigner transform."""

    def __init__(
        self,
        harmonic_transform: InverseSpinLayer,
        fourier_transform: FourierLayer,
        **kwargs,
    ):
        if kwargs.pop("trainable", False):
            raise ValueError("This layer is not trainable")
        super().__init__(trainable=False, **kwargs)

        self._harmonic = harmonic_transform
        self._fourier = fourier_transform
        self._lfactor = tf.constant(0)

    def __call__(self, tensor: tf.Tensor) -> tf.Tensor:
        return super().__call__(tensor)

    def build(self, input_shape):
        from tensossht.sampling import Axis, ImageAxes

        assert isinstance(self._harmonic.out_axes, ImageAxes)
        self._harmonic.out_axes = self._harmonic.out_axes.shift(
            len(input_shape), Axis.SPIN
        )
        self._harmonic.build(input_shape)
        harmonic_shape = self._harmonic.compute_output_shape(input_shape)
        self._fourier.build(harmonic_shape)
        hsampling = self._harmonic.harmonic_sampling(input_shape)
        rdtype = tf.dtypes.as_dtype(self.dtype).real_dtype
        cdtype = tf.complex(tf.zeros(0, dtype=rdtype), tf.zeros(0, dtype=rdtype)).dtype
        nspins = self._fourier.compute_output_shape(harmonic_shape)[
            self._fourier.out_axis
        ]
        self._factor = (
            nspins
            / _lfactor(
                hsampling=hsampling,
                axes=cast(HarmonicAxes, self._harmonic.in_axes),
                input_shape=input_shape,
                dtype=cdtype,
            )
            * _sfactor(
                hsampling=hsampling,
                axes=cast(HarmonicAxes, self._harmonic.in_axes),
                input_shape=input_shape,
                dtype=cdtype,
            )
        )

    @tf.function
    def call(self, inputs: tf.Tensor) -> tf.Tensor:
        gamma_fourier = self._harmonic.__call__(inputs * self._factor)
        if not self._fourier.is_real:
            gamma_fourier = tf.signal.ifftshift(gamma_fourier, self._fourier.axis)
        return self._fourier(gamma_fourier)


def wigner_layer(
    is_forward: bool = True,
    is_real: bool = False,
    is_odd_spin: bool = True,
    sampling: Union[str, ImageSamplingSchemes] = "mw",
    theta_dim: int = -3,
    phi_dim: int = -2,
    gamma_dim: int = -1,
    spin_dim: int = -2,
    coeff_dim: int = -1,
    dtype: Union[str, np.dtype, tf.DType] = tf.float64,
    **kwargs,
) -> tf.keras.layers.Layer:
    """Factory for wigner transform layers.

    Args:
        is_forward: If ``True``, performs image to Wigner space transform. If ``False``,
            performs Wigner to image space transform.
        is_real: If ``True``, the image-space signal is real.
        is_odd_spin: Only useful for inverse transforms to real image-space signals. If
            ``True``, recovers an odd number of spin functions. Otherwise, recovers an
            even number of spin functions.
        sampling: Real-space sampling.
        theta_dim: Index of the :math:`\\theta` dimension.
        phi_dim: Index of the :math:`\\phi` dimension.
        gamma_dim: Index of the :math:`\\gamma` dimension.
        spin_dim: Index of the spin dimension.
        coeff_dim: Index of the coefficients dimension.
        dtype: Underlying type of floating point operations. Only the bit-size of the
            floating point matters. A complex ``dtype`` can be given equivalently.
    """
    from tensossht.layers.harmonic_transforms import ForwardSpinLayer, InverseSpinLayer

    rdtype = tf.dtypes.as_dtype(dtype).real_dtype
    cdtype = tf.complex(tf.zeros(0, dtype=rdtype), tf.zeros(0, dtype=rdtype)).dtype
    fft = FourierLayer(
        is_forward=is_forward,
        is_real=is_real,
        axis=gamma_dim if is_forward else -1,
        out_axis=-1 if is_forward else gamma_dim,
        dtype=rdtype if is_real else cdtype,
        is_odd_spin=is_odd_spin,
        **kwargs,
    )
    HTL = ForwardSpinLayer if is_forward else InverseSpinLayer
    ht = HTL(
        sampling=sampling,
        theta_dim=theta_dim,
        phi_dim=phi_dim,
        spin_dim=gamma_dim if is_forward else spin_dim,
        out_spin_dim=spin_dim if is_forward else gamma_dim,
        coeff_dim=coeff_dim,
        flip_spin=True,
        centered_spin=not is_real,
        dtype=cdtype,
        **kwargs,
    )
    WTL = ForwardWignerLayer if is_forward else InverseWignerLayer
    return WTL(  # type: ignore
        fourier_transform=fft, harmonic_transform=ht, dtype=fft.dtype, **kwargs
    )


def _lfactor(
    hsampling: HarmonicSampling,
    axes: HarmonicAxes,
    input_shape: Sequence[int],
    dtype: Union[str, np.dtype, tf.DType] = tf.float64,
) -> tf.Tensor:
    assert axes.spin is not None
    rdtype = tf.dtypes.as_dtype(dtype).real_dtype
    llabels = hsampling.llabels[: hsampling.ncoeffs // hsampling.nspins]
    lfactor = (
        tf.constant(4 * np.pi, rdtype)
        * tf.math.sqrt(tf.constant(np.pi, rdtype))
        / tf.math.sqrt(tf.cast(2 * llabels + 1, rdtype))
    )
    return tf.reshape(
        tf.cast(lfactor, dtype),
        tf.one_hot(
            axes.coeff % (len(input_shape) - 1),
            len(input_shape) - 1,
            on_value=-1,
            off_value=1,
        ),
    )


def _sfactor(
    hsampling: HarmonicSampling,
    axes: HarmonicAxes,
    input_shape: Sequence[int],
    dtype: Union[str, np.dtype, tf.DType] = tf.float64,
) -> tf.Tensor:
    assert axes.spin is not None
    slabels = tf.reshape(hsampling.slabels, [hsampling.nspins, -1])[:, 0]
    return tf.reshape(
        tf.cast(1 - 2 * (slabels % 2), dtype),
        tf.one_hot(
            axes.spin % (len(input_shape) - 1),
            len(input_shape) - 1,
            on_value=-1,
            off_value=1,
        ),
    )
