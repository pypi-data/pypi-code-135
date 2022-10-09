from pathlib import Path
from typing import Callable, Optional, Tuple, Union, cast

import numpy as np
import tensorflow as tf

from tensossht.sampling import (
    HarmonicAxes,
    HarmonicSampling,
    ImageAxes,
    ImageSamplingBase,
    ImageSamplingSchemes,
)

__doc__ = Path(__file__).with_suffix(".rst").read_text()


class BaseHarmonicTransformLayer(tf.keras.layers.Layer):
    def __init__(
        self,
        is_real: bool = False,
        sampling: Union[str, ImageSamplingSchemes, ImageSamplingBase] = "mw",
        spin: int = 0,
        dtype: Union[str, np.dtype, tf.DType] = tf.float32,
        in_axes: Optional[Union[HarmonicAxes, ImageAxes]] = None,
        out_axes: Optional[Union[HarmonicAxes, ImageAxes]] = None,
        **kwargs,
    ):
        from tensossht.sampling import image_sampling_scheme

        rdtype = tf.dtypes.as_dtype(dtype).real_dtype
        cdtype = tf.complex(tf.zeros(0, dtype=rdtype), tf.zeros(0, dtype=rdtype)).dtype

        if is_real and spin != 0:
            raise ValueError("Non-zero spins are complex")

        if kwargs.pop("trainable", False):
            raise ValueError("This layer is not trainable")

        super().__init__(trainable=False, dtype=rdtype if is_real else cdtype, **kwargs)
        self.is_real = is_real
        self.sampling = image_sampling_scheme(sampling)
        self.spin = spin
        self.transform: Callable = BaseHarmonicTransformLayer._build_not_called
        self.in_axes = in_axes
        self.out_axes = out_axes

    def __call__(self, tensor: tf.Tensor) -> tf.Tensor:
        return super().__call__(tensor)

    def call(self, inputs) -> tf.Tensor:
        in_axes = {} if self.in_axes is None else self.in_axes._asdict()
        in_axes = {f"{k}_dim": v for k, v in in_axes.items() if v is not None}
        out_axes = {} if self.out_axes is None else self.out_axes._asdict()
        out_axes = {f"{k}_dim": v for k, v in out_axes.items() if v is not None}
        if "spin_dim" in out_axes:
            out_axes["out_spin_dim"] = out_axes.pop("spin_dim")

        return self.transform(inputs, **in_axes, **out_axes)

    @staticmethod
    def _build_not_called(
        x: tf.Tensor, theta_dim: int = -2, phi_dim: int = -1, coeff_dim: int = -1
    ) -> tf.Tensor:
        raise RuntimeError("Build was not called.")

    def get_config(self):
        config = super().get_config()
        config.update(
            dict(
                is_real=self.is_real,
                sampling=self.sampling.name,
                spin=self.spin,
                in_axes=None if self.in_axes is None else self.in_axes._asdict(),
                out_axes=None if self.out_axes is None else self.out_axes._asdict(),
            )
        )
        return config

    @classmethod
    def from_config(cls, config):
        if config["in_axes"] is not None and "phi" in config["in_axes"]:
            config["in_axes"] = ImageAxes(**config.pop("in_axes"))
        elif config["in_axes"] is not None:
            config["in_axes"] = HarmonicAxes(**config.pop("in_axes"))
        if config["out_axes"] is not None and "phi" in config["out_axes"]:
            config["out_axes"] = ImageAxes(**config.pop("out_axes"))
        elif config["out_axes"] is not None:
            config["out_axes"] = HarmonicAxes(**config.pop("out_axes"))
        return cls(**config)


class BaseHarmonicSpinTransformLayer(BaseHarmonicTransformLayer):
    def __init__(
        self,
        sampling: Union[str, ImageSamplingSchemes] = "mw",
        spin: int = 0,
        dtype: Union[str, np.dtype, tf.DType] = tf.float32,
        in_axes: Optional[Union[HarmonicAxes, ImageAxes]] = None,
        out_axes: Optional[Union[HarmonicAxes, ImageAxes]] = None,
        flip_spin: bool = False,
        centered_spin: bool = True,
        **kwargs,
    ):
        super().__init__(
            is_real=False,
            sampling=sampling,
            spin=spin,
            dtype=dtype,
            out_axes=out_axes,
            in_axes=in_axes,
            **kwargs,
        )
        self.flip_spin = flip_spin
        """Flip spin direction, useful for wigner transform."""
        self.centered_spin = centered_spin
        """Defines how the spins are determined from the shape of the input.

        If `True`, then the range is :math:`[-n, n]`. If `False`, then it is
        :math:`[0, n]`
        """

    def get_config(self):
        config = super().get_config()
        config.update(dict(flip_spin=self.flip_spin, centered_spin=self.centered_spin))
        return config

    def spin_range(self, axis_size: int) -> Tuple[int, int]:
        if self.centered_spin and axis_size % 2 != 1:
            raise ValueError(
                "Expected odd number of spin channels "
                "since the channels are centered around 0."
            )
        elif self.centered_spin:
            nspins = (axis_size - 1) // 2
            return self.spin - nspins, self.spin + nspins
        return 0, axis_size - 1


class InverseLayer(BaseHarmonicTransformLayer):
    def __init__(
        self,
        is_real: bool = False,
        sampling: Union[str, ImageSamplingSchemes, ImageSamplingBase] = "mw",
        spin: int = 0,
        dtype: Union[str, np.dtype, tf.DType] = tf.float32,
        theta_dim: int = -2,
        phi_dim: int = -1,
        coeff_dim: int = -1,
        **kwargs,
    ):
        return super().__init__(
            is_real=is_real,
            sampling=sampling,
            spin=spin,
            dtype=dtype,
            in_axes=HarmonicAxes(coeff=coeff_dim),
            out_axes=ImageAxes(phi=phi_dim, theta=theta_dim),
            **kwargs,
        )

    def build(self, shape: tf.TensorShape) -> None:
        from tensossht.transforms.inverse import inverse_transform

        axes = (
            cast(HarmonicAxes, self.in_axes)
            if self.in_axes is not None
            else HarmonicAxes(coeff=-1)
        )
        if not self.is_real:
            lmax = int(np.sqrt(shape[axes.coeff] + self.spin * self.spin))
            assert lmax * lmax - self.spin * self.spin == shape[axes.coeff]
            mmin = None
        else:
            lmax = int(np.sqrt(1 + 8 * shape[axes.coeff]) - 1) // 2
            assert lmax * (lmax + 1) == 2 * shape[axes.coeff]
            mmin = 0

        self.transform = inverse_transform(
            lmax, mmin=mmin, spin=self.spin, sampling=self.sampling, dtype=self.dtype
        )


class InverseSpinLayer(BaseHarmonicSpinTransformLayer):
    def __init__(
        self,
        sampling: Union[str, ImageSamplingSchemes] = "mw",
        dtype: Union[str, np.dtype, tf.DType] = tf.float32,
        spin_dim: int = -2,
        coeff_dim: int = -1,
        out_spin_dim: int = -3,
        theta_dim: int = -2,
        phi_dim: int = -1,
        spin: int = 0,
        **kwargs,
    ):
        super().__init__(
            sampling=sampling,
            spin=spin,
            dtype=dtype,
            in_axes=HarmonicAxes(coeff=coeff_dim, spin=spin_dim),
            out_axes=ImageAxes(phi=phi_dim, theta=theta_dim, spin=out_spin_dim),
            **kwargs,
        )

    def harmonic_sampling(self, shape: tf.TensorShape) -> HarmonicSampling:
        """Figures harmonic sampling from shape of the input tensor."""
        from tensossht.sampling import harmonic_sampling_scheme

        axes = (
            cast(HarmonicAxes, self.in_axes)
            if self.in_axes is not None
            else HarmonicAxes(coeff=-1)
        )
        lmax = int(np.sqrt(shape[axes.coeff]))
        assert lmax * lmax == shape[axes.coeff]

        smin, smax = self.spin_range(shape[axes.spin])
        hsampling = harmonic_sampling_scheme(
            lmax, mmin=None, smin=smin, smax=smax, compact_spin=False
        )
        if self.flip_spin:
            labels = tf.concat((hsampling.labels[:2], -hsampling.labels[2:]), axis=0)
            hsampling = harmonic_sampling_scheme(labels=labels)
        return hsampling

    def build(self, shape: tf.TensorShape) -> None:
        from tensossht.transforms.inverse import inverse_transform

        hsampling = self.harmonic_sampling(shape)
        self.transform = inverse_transform(
            hsampling, sampling=self.sampling, dtype=self.dtype
        )

    def get_config(self):
        config = super().get_config()
        config.update(dict(flip_spin=self.flip_spin))
        return config

    def compute_output_shape(self, input_shape: tf.TensorShape) -> tf.TensorShape:
        assert isinstance(self.in_axes, HarmonicAxes)
        assert self.in_axes.spin is not None
        in_axes = self.in_axes % len(input_shape)
        result = [j for i, j in enumerate(input_shape) if i not in in_axes]

        hsampling = self.harmonic_sampling(input_shape)
        nthetas, nphis = self.sampling.value(hsampling.lmax).shape

        result += [hsampling.nspins, nthetas, nphis]
        assert isinstance(self.out_axes, ImageAxes)
        permutation = ImageAxes(spin=-3, theta=-2, phi=-1).permutation(
            self.out_axes, len(input_shape) + 1
        )
        return tf.TensorShape([result[i] for i in permutation])


class ForwardLayer(BaseHarmonicTransformLayer):
    def __init__(
        self,
        is_real: bool = False,
        sampling: Union[str, ImageSamplingSchemes] = "mw",
        spin: int = 0,
        dtype: Union[str, np.dtype, tf.DType] = tf.float32,
        theta_dim: int = -2,
        phi_dim: int = -1,
        coeff_dim: int = -1,
        **kwargs,
    ):
        return super().__init__(
            is_real=is_real,
            sampling=sampling,
            spin=spin,
            dtype=dtype,
            out_axes=HarmonicAxes(coeff=coeff_dim),
            in_axes=ImageAxes(phi=phi_dim, theta=theta_dim),
            **kwargs,
        )

    def build(self, shape: tf.TensorShape) -> None:
        from tensossht.transforms.forward import forward_transform

        mmin = 0 if self.is_real else None
        axes = (
            cast(ImageAxes, self.in_axes)
            if self.in_axes is not None
            else ImageAxes(theta=-2, phi=-1)
        )
        if self.sampling == ImageSamplingSchemes.MW:
            lmax = shape[axes.theta]
        else:
            lmax = shape[axes.theta] - 1
        self.transform = forward_transform(
            lmax, mmin=mmin, spin=self.spin, sampling=self.sampling, dtype=self.dtype
        )


class ForwardSpinLayer(BaseHarmonicSpinTransformLayer):
    def __init__(
        self,
        sampling: Union[str, ImageSamplingSchemes] = "mw",
        dtype: Union[str, np.dtype, tf.DType] = tf.float32,
        spin_dim: int = -3,
        theta_dim: int = -2,
        phi_dim: int = -1,
        coeff_dim: int = -1,
        out_spin_dim: int = -2,
        spin: int = 0,
        **kwargs,
    ):
        super().__init__(
            sampling=sampling,
            spin=spin,
            dtype=dtype,
            out_axes=HarmonicAxes(coeff=coeff_dim, spin=out_spin_dim),
            in_axes=ImageAxes(phi=phi_dim, theta=theta_dim, spin=spin_dim),
            **kwargs,
        )

    def harmonic_sampling(self, shape: tf.TensorShape) -> HarmonicSampling:
        """Figures harmonic sampling from shape of the input tensor."""
        from tensossht.sampling import harmonic_sampling_scheme

        axes = (
            cast(ImageAxes, self.in_axes)
            if self.in_axes is not None
            else ImageAxes(theta=-2, phi=-1)
        )
        if self.sampling == ImageSamplingSchemes.MW:
            lmax = shape[axes.theta]
        else:
            lmax = shape[axes.theta] - 1
        smin, smax = self.spin_range(shape[axes.spin])
        hsampling = harmonic_sampling_scheme(
            lmax, mmin=None, smin=smin, smax=smax, compact_spin=False
        )
        if self.flip_spin:
            labels = tf.concat((hsampling.labels[:2], -hsampling.labels[2:]), axis=0)
            hsampling = harmonic_sampling_scheme(labels=labels)
        return hsampling

    def build(self, shape: tf.TensorShape) -> None:
        from tensossht.transforms.forward import forward_transform

        hsampling = self.harmonic_sampling(shape)
        self.transform = forward_transform(
            hsampling, dtype=self.dtype, sampling=self.sampling
        )
