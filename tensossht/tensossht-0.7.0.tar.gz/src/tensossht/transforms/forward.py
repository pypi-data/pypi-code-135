from typing import Callable, Optional, Type, Union

import numpy as np
import tensorflow as tf

from tensossht.references import REFERENCES
from tensossht.sampling import HarmonicAxes, ImageAxes, ImageSamplingSchemes
from tensossht.transforms.gmm_to_coeffs import GmmToCoeffs


class ForwardTransformBase:
    f"""Forward Spherical Harmonic Transform.

    Converts image-space signals to harmonic space signals, following [McEwen, Wiaux
    (2011)], section IV.D.

    {REFERENCES['MW']}
    """

    def __init__(
        self, images_to_fmm: Callable, fmm_to_gmm: Callable, gmm_to_coeffs: GmmToCoeffs
    ):
        self.images_to_fmm = images_to_fmm
        self.fmm_to_gmm = fmm_to_gmm
        self.gmm_to_coeffs = gmm_to_coeffs

    def _call(
        self, images: tf.Tensor, in_axes: ImageAxes, out_axes: HarmonicAxes
    ) -> tf.Tensor:
        from tensossht.sampling import Axis

        fmm = self.images_to_fmm(images, in_axes)
        tfmm = in_axes.shift(len(fmm.shape), Axis.PHI, Axis.THETA).transpose(
            fmm, in_axes.shift(len(fmm.shape), Axis.SPIN, Axis.PHI, Axis.THETA)
        )
        gmm = self.fmm_to_gmm(tfmm)
        coeff = self.gmm_to_coeffs(gmm)
        return HarmonicAxes(
            coeff=-1, spin=-2 if in_axes.spin is not None else None
        ).transpose(coeff, out_axes)


class ForwardTransform(ForwardTransformBase):
    f"""Forward Spherical Harmonic Transform.

    Converts image-space signals to harmonic space signals, following [McEwen, Wiaux
    (2011)], section IV.D.

    {REFERENCES['MW']}
    """

    @tf.function
    def __call__(
        self,
        images: tf.Tensor,
        theta_dim: int = -2,
        phi_dim: int = -1,
        coeff_dim: int = -1,
    ) -> tf.Tensor:
        return super()._call(
            images,
            ImageAxes(theta=theta_dim, phi=phi_dim, spin=None),
            HarmonicAxes(coeff=coeff_dim, spin=None),
        )


class ForwardSpinTransform(ForwardTransformBase):
    @tf.function
    def __call__(
        self,
        images: tf.Tensor,
        spin_dim: int = -3,
        theta_dim: int = -2,
        phi_dim: int = -1,
        out_spin_dim: int = -2,
        coeff_dim: int = -1,
    ) -> tf.Tensor:
        return super()._call(
            images,
            ImageAxes(theta=theta_dim, phi=phi_dim, spin=spin_dim),
            HarmonicAxes(coeff=coeff_dim, spin=out_spin_dim),
        )


def forward_transform(
    lmax: Optional[Union[tf.Tensor, int]] = None,
    lmin: Optional[int] = None,
    mmax: Optional[int] = None,
    mmin: Optional[int] = None,
    smin: Optional[int] = None,
    smax: Optional[int] = None,
    spin: Optional[int] = None,
    compact_spin: Optional[bool] = None,
    labels: Optional[tf.Tensor] = None,
    dtype: Union[str, np.dtype, tf.DType] = tf.float32,
    sampling: Union[str, ImageSamplingSchemes] = ImageSamplingSchemes.MW,
) -> Callable:
    """Factory function for the forward transform.

    Args:
        lmax: Maximum degree of the spherical harmonics.
        lmin: Minimum degree of the spherical harmonics, defaults to 0 if ``None`` or
           not specified.
        mmax: Maximum order of the spherical harmonics. Defaults to ``lmax`` if
           ``None`` or not specified.
        mmin: Minimum order of the spherical harmonics. Defaults to ``-lmax`` if
           ``None`` or not specified.
        smax: Maximum spin for the spin-spherical harmonics.
           - if `spin` is not specified, than defaults to ``lmax``
           - if `spin` is specified, then defaults to `spin`
        smin: Minimum spin for the spin-spherical harmonics.
            - if `spin` is not specified, than defaults to ``-lmax``
            - if `spin` is specified, then defaults to `spin`
        spin: shortcut to specify ``smin = smax = spin``.
        compact_spin: Whether to adopt a compact memory representation of spins or not.
            - if `spin` is specified or ``smin == smax``, defaults ``True`` (single-spin
              transform)
            - otherwise defaults to ``False`` (multispin transform)
        dtype: Default underlying float
        sampling: Image-space sampling
    """
    from tensossht.sampling import harmonic_sampling_scheme, image_sampling_scheme
    from tensossht.transforms.fmm_to_gmm import fmm_to_gmm
    from tensossht.transforms.gmm_to_coeffs import gmm_to_coeffs
    from tensossht.transforms.images_to_fmm import images_to_fmm

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
            Type[ForwardSpinTransform], Type[ForwardTransform]
        ] = ForwardSpinTransform
    elif not hsampling.is_multi_spin:
        Transform = ForwardTransform
    else:
        raise NotImplementedError("Non-separable multi-spin transform not implemented")
    return Transform(
        images_to_fmm(hsampling, sampling, rdtype),
        fmm_to_gmm=fmm_to_gmm(hsampling.lmax, rdtype, hsampling.is_real),
        gmm_to_coeffs=gmm_to_coeffs(hsampling, rdtype),
    )
