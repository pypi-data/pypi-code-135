"""
==================================
Image and Harmonic Space Samplings
==================================

This modules contains helpers to define the different harmonic-space and image space
samplings.

Creating Samplings
==================

.. autofunction :: tensossht.sampling.equiangular
.. autofunction :: tensossht.sampling.image_sampling_scheme
.. autofunction :: tensossht.sampling.harmonic_sampling_scheme
.. autofunction :: tensossht.sampling.wignerd_labels
.. autofunction :: tensossht.sampling.symmetric_labels
.. autofunction :: tensossht.sampling.spin_legendre_labels
.. autofunction :: tensossht.sampling.legendre_labels

Manipulating Samplings
======================

.. autofunction :: tensossht.sampling.transpose
.. autofunction :: tensossht.sampling.equiangular_shape

Data structures
===============

.. autoclass :: tensossht.sampling.HarmonicAxes
.. autoclass :: tensossht.sampling.MW
.. autoclass :: tensossht.sampling.MWSS
.. autoclass :: tensossht.sampling.EquiangularShape
.. autoclass :: tensossht.sampling.ImageSamplingBase
"""
from enum import Enum
from functools import singledispatch
from typing import (
    Any,
    Iterable,
    List,
    NamedTuple,
    Optional,
    Sequence,
    Tuple,
    Union,
    cast,
)

import numpy as np
import tensorflow as tf

from tensossht.typing import Array, TFArray

LType = Union[int, Array, tf.Variable]


def equiangular_theta(
    lmax: LType,
    dtype: Union[str, np.dtype, tf.DType] = tf.float64,
) -> TFArray:
    """Equiangular theta sampling.

    .. math::

        \\theta = \\pi\\frac{2n + 1}{2l_\\text{max} - 1};
        \\quad\\text{for}\\, n \\in [0, l_\\text{max}[

    Example:

        >>> from pytest import approx
        >>> from numpy import pi
        >>> from tensossht.sampling import equiangular_theta
        >>> for lmax in [1, 5, 10]:
        ...     expected = [(2 * t + 1) * pi / (2 * lmax - 1) for t in range(lmax)]
        ...     assert equiangular_theta(lmax).numpy() == approx(expected)

    """
    if lmax < 1:
        raise ValueError("lmax cannot be smaller than 1")

    step = tf.constant(np.pi / (2 * tf.constant(lmax, dtype=dtype) - 1), dtype=dtype)
    return tf.range(step, tf.constant(np.pi, dtype=dtype) + step, 2 * step)


def symmetric_theta(
    lmax: LType,
    dtype: Union[str, np.dtype, tf.DType] = tf.float64,
) -> TFArray:
    """Symmetric theta sampling.

    .. math::

        \\theta = \\pi\\frac{n}{l_\\text{max}};
        \\quad\\text{for}\\, n \\in [0, l_\\text{max} + 1[

    Example:

        >>> from pytest import approx
        >>> from tensossht.sampling import symmetric_theta
        >>> for lmax in [1, 5, 10]:
        ...     expected = [t * np.pi / lmax for t in range(lmax + 1)]
        ...     assert symmetric_theta(lmax).numpy() == approx(expected)

    """
    if lmax < 1:
        raise ValueError("lmax cannot be smaller than 1")

    step = tf.constant(np.pi / tf.constant(lmax, dtype=dtype), dtype=dtype)
    return tf.range(tf.constant(np.pi, dtype=dtype) + step, delta=step)


def equiangular_phi(
    lmax: LType,
    dtype: Union[str, np.dtype, tf.DType] = tf.float64,
) -> TFArray:
    """Equiangular phi sampling.

    .. math::

        \\phi = 2\\pi\\frac{n}{2l_\\text{max} - 1};
        \\quad\\text{for}\\, n \\in [0, 2l_\\text{max} - 1[

    Example:

        >>> from pytest import approx
        >>> from numpy import pi
        >>> from tensossht.sampling import equiangular_phi
        >>> for lmax in [1, 5, 10]:
        ...     expected = [(2 * pi * p) / (2 * lmax - 1) for p in range(2 * lmax - 1)]
        ...     assert equiangular_phi(lmax).numpy() == approx(expected)

    """
    if lmax < 1:
        raise ValueError("lmax cannot be smaller than 1")

    step = 2 * tf.constant(np.pi, dtype=dtype) / tf.constant(2 * lmax - 1, dtype=dtype)
    return tf.range(2 * tf.constant(np.pi, dtype=dtype) - step * 0.5, delta=step)


def symmetric_phi(
    lmax: LType,
    dtype: Union[str, np.dtype, tf.DType] = tf.float64,
) -> TFArray:
    """Symmetric phi sampling.

    .. math::

        \\phi = 2\\pi\\frac{n}{2l_\\text{max}};
        \\quad\\text{for}\\, n \\in [0, 2l_\\text{max}[

    Example:

        >>> from pytest import approx
        >>> from tensossht.sampling import symmetric_phi
        >>> for lmax in [1, 5, 10]:
        ...     expected = [np.pi * p / lmax for p in range(2 * lmax)]
        ...     assert symmetric_phi(lmax).numpy() == approx(expected)

    """
    if lmax < 1:
        raise ValueError("lmax cannot be smaller than 1")

    step = tf.constant(np.pi / tf.constant(lmax, dtype=dtype), dtype=dtype)
    return tf.range(2 * tf.constant(np.pi, dtype=dtype) - 0.5 * step, delta=step)


class EquiangularShape(NamedTuple):
    theta: int
    phi: int


def equiangular_shape(lmax: int) -> EquiangularShape:
    """Shape of equiangular samples.

    Example:

        >>> from tensossht.sampling import (
        ...     equiangular_phi, equiangular_theta, equiangular_shape
        ... )
        >>> len(equiangular_theta(5)) == equiangular_shape(5)[0]
        True
        >>> len(equiangular_theta(5)) == equiangular_shape(5).theta
        True
        >>> len(equiangular_phi(5)) == equiangular_shape(5)[1]
        True
        >>> len(equiangular_phi(5)) == equiangular_shape(5).phi
        True

    """
    return EquiangularShape(lmax, 2 * lmax - 1)


def equiangular(
    lmax: int, dtype: Union[str, np.dtype, tf.DType] = tf.float64
) -> TFArray:
    """Equiangular samples.

    Example:

        >>> from tensossht.sampling import equiangular
        >>> equiangular(3).numpy().round(2)
        array([[[0.63, 0.63, 0.63, 0.63, 0.63],
                [1.88, 1.88, 1.88, 1.88, 1.88],
                [3.14, 3.14, 3.14, 3.14, 3.14]],
        <BLANKLINE>
               [[0.  , 1.26, 2.51, 3.77, 5.03],
                [0.  , 1.26, 2.51, 3.77, 5.03],
                [0.  , 1.26, 2.51, 3.77, 5.03]]])

    """
    thetas = equiangular_theta(lmax, dtype)
    phis = equiangular_phi(lmax, dtype)

    return tf.concat(
        (
            tf.repeat(thetas[None, :, None], [phis.shape[0]], axis=2),
            tf.repeat(phis[None, None, :], [thetas.shape[0]], axis=1),
        ),
        axis=0,
    )


class ImageSamplingBase:
    def __init__(self, lmax: int, dtype: tf.DType = tf.float64):
        self.lmax = lmax
        self.dtype = dtype

    def __repr__(self):
        return f"{self.__class__.__name__}(lmax={self.lmax}, dtype={self.dtype!r})"

    @property
    def thetas(_):
        raise NotImplementedError()

    @property
    def phis(_):
        raise NotImplementedError()

    @property
    def grid(self):
        """Image-space grid."""
        thetas = self.thetas
        phis = self.phis
        return tf.concat(
            (
                tf.repeat(thetas[None, :, None], [phis.shape[0]], axis=2),
                tf.repeat(phis[None, None, :], [thetas.shape[0]], axis=1),
            ),
            axis=0,
        )

    @property
    def points(self):
        """Image-space points."""
        return tf.transpose(tf.reshape(self.grid, (2, -1)))

    @property
    def shape(self):
        """Theta and phi shapes."""
        return len(self.thetas), len(self.phis)


class MW(ImageSamplingBase):
    """McEwen - Viaux image-space sampling."""

    @property
    def thetas(self):
        return equiangular_theta(lmax=self.lmax, dtype=self.dtype)

    @property
    def phis(self):
        return equiangular_phi(lmax=self.lmax, dtype=self.dtype)

    @property
    def shape(self):
        """Theta and phi shapes."""
        return self.lmax, 2 * self.lmax - 1


class MWSS(ImageSamplingBase):
    """McEwen - Viaux symmetric image-space sampling."""

    @property
    def thetas(self):
        return symmetric_theta(lmax=self.lmax, dtype=self.dtype)

    @property
    def phis(self):
        return symmetric_phi(lmax=self.lmax, dtype=self.dtype)

    @property
    def shape(self):
        """Theta and phi shapes."""
        return self.lmax + 1, 2 * self.lmax


class ImageSamplingSchemes(Enum):
    """Helper for factories that need a sampling scheme as input.

    Example:

        >>> from tensossht import sampling
        >>> mw = sampling.ImageSamplingSchemes.MW
        >>> assert mw == sampling.image_sampling_scheme("mw")
        >>> assert mw.value is sampling.MW
        >>> mwss = sampling.ImageSamplingSchemes['MWSS']
        >>> assert mwss == sampling.image_sampling_scheme("mwss")
        >>> assert mwss.value is sampling.MWSS

    """

    MW = MW
    MWSS = MWSS


@singledispatch
def image_sampling_scheme(sampling) -> ImageSamplingSchemes:
    raise RuntimeError(f"Unexpected input type {(sampling)}")


@image_sampling_scheme.register(ImageSamplingSchemes)
def _image_sampling_scheme0(sampling: ImageSamplingSchemes) -> ImageSamplingSchemes:
    return sampling


@image_sampling_scheme.register(str)
def _image_sampling_scheme1(sampling: str) -> ImageSamplingSchemes:
    for smpl in ImageSamplingSchemes:
        if smpl.name.lower() == sampling.lower():
            return smpl
    else:
        raise ValueError(f"Unkown sampling scheme {sampling}")


@image_sampling_scheme.register(ImageSamplingBase)
def _image_sampling_scheme2(sampling: ImageSamplingBase) -> ImageSamplingSchemes:
    for smpl in ImageSamplingSchemes:
        if isinstance(sampling, smpl.value):
            return smpl
    else:
        raise ValueError(f"Unkown sampling scheme {sampling}")


class HarmonicSampling(NamedTuple):
    """Sampling in harmonic space.

    I.e. which spherical harmonics are included in the basis.
    """

    lmax: int
    lmin: int
    mmax: int
    mmin: int
    smin: int
    smax: int
    is_separable_spin: bool
    labels: TFArray

    @property
    def is_real(self):
        return self.mmin >= 0 and self.smin == 0 and self.smax == 0

    @property
    def is_complex(self):
        return not self.is_real

    @property
    def is_multi_spin(self):
        return self.smin != self.smax

    @property
    def is_single_spin(self):
        return not self.is_multi_spin

    @property
    def llabels(self):
        return self.labels[0]

    @property
    def mlabels(self):
        return self.labels[1]

    @property
    def slabels(self):
        return self.labels[2]

    @property
    def ncoeffs(self):
        return self.labels.shape[1]

    @property
    def nspins(self):
        return self.smax - self.smin + 1

    @property
    def valid(self):
        """Whether the tuple (l, m, s) is valid.

        .. math::

            l >= 0

            |m| <= l

            |s| <= l
        """
        return tf.logical_and(
            self.llabels >= 0,
            tf.logical_and(
                tf.math.abs(self.mlabels) <= self.llabels,
                tf.math.abs(self.slabels) <= self.llabels,
            ),
        )

    @property
    def spins(self) -> Union[int, TFArray]:
        """Range of spins in the sampling."""
        if self.is_multi_spin and self.is_separable_spin:
            return tf.reshape(self.slabels, (self.nspins, -1))[:, 0]
        elif self.smin == self.smax:
            return self.smin
        raise AttributeError("Cannot compute spin range")


def harmonic_sampling_scheme(
    lmax: Optional[Union[int, Array, HarmonicSampling]] = None,
    lmin: Optional[int] = None,
    mmax: Optional[int] = None,
    mmin: Optional[int] = None,
    smax: Optional[int] = None,
    smin: Optional[int] = None,
    spin: Optional[int] = None,
    labels: Optional[Array] = None,
    compact_spin: Optional[bool] = None,
) -> HarmonicSampling:
    """Basis functions in harmonic space.

    Args:
        lmax:
            Maximum degree, :math:`l < l_\\mathrm{max}`. For practical purposes, the
            first argument of the function can also be the 3 by n tensor ``labels``, or
            a :py:class:`~tensossht.sampling.HarmonicSampling` instance.
        lmin:
            minimum degree, :math:`l \\geq l_\\mathrm{min}`
        mmax:
            Maximum order, :math:`m \\leq m_\\mathrm{max}`
        mmin:
            Maximum order, :math:`m \\geq m_\\mathrm{min}`
        smax:
            Maximum spin, :math:`s \\leq s_\\mathrm{max}`
        smin:
            Maximum spin, :math:`s \\geq s_\\mathrm{min}`
        spin:
            shortcut for :math:`s = s_\\mathrm{min} = s_\\mathrm{max}`
        labels:
            3 by n tensor listing the :math:`(l, m, s)` triplets. Alternative to
            specifying ``lmax`` and friends.
        compact_spin:
            If ``True``, the representation will be memory efficient. If ``False``, the
            representation is sucht the spin dimension can be separated from the
            other coefficients. The latter is generally more practical, especially for
            for smaller ``smax``. Ignored if ``labels`` are given.
    """
    if isinstance(lmax, HarmonicSampling):
        return lmax
    # labels passed as first and only argument
    if (
        lmin is None
        and mmax is None
        and mmin is None
        and smax is None
        and smin is None
        and spin is None
        and labels is None
        and len(getattr(lmax, "shape", ())) == 2
    ):
        return harmonic_sampling_scheme(labels=lmax)

    if lmax is None and labels is None:
        raise ValueError("One of lmax or labels must be given")
    if lmax is not None and labels is not None:
        raise ValueError("Only one of lmax or labels can be given")
    if lmax is not None and len(tf.shape(lmax)) == 2 and tf.shape(lmax)[0] in (2, 3):
        lmax, labels = None, cast(Array, lmax)
    if lmax is not None:
        labels = _figure_labels(lmax, lmin, mmax, mmin, smax, smin, spin, compact_spin)
    assert labels is not None
    if len(labels.shape) != 2 or labels.shape[0] not in (2, 3):
        raise ValueError("labels outght to be a 2 or 3 by n matrix")
    if labels.shape[0] == 2:
        labels = tf.concat((labels, tf.zeros_like(labels[:1])), axis=0)
    assert labels is not None
    lmax = int(tf.reduce_max(labels[0])) + 1
    lmin = int(tf.reduce_min(labels[0]))
    mmax = int(tf.reduce_max(labels[1]))
    mmin = int(tf.reduce_min(labels[1]))
    smax = int(tf.reduce_max(labels[2]))
    smin = int(tf.reduce_min(labels[2]))
    assert labels is not None
    assert lmin is not None and lmax is not None
    assert mmin is not None and mmax is not None
    assert smin is not None and smax is not None

    iss = is_separable_spin(smin, smax, labels)
    return HarmonicSampling(lmax, lmin, mmax, mmin, smin, smax, iss, labels)


def _figure_labels(
    lmax: int,
    lmin: Optional[int] = None,
    mmax: Optional[int] = None,
    mmin: Optional[int] = None,
    smax: Optional[int] = None,
    smin: Optional[int] = None,
    spin: Optional[int] = None,
    compact_spin: Optional[bool] = None,
) -> TFArray:
    if lmax <= 0:
        raise ValueError("lmax must be strictly positive.")
    if spin is not None and smin is not None and spin != smin:
        raise ValueError("Only one of spin or smin should be given")
    if spin is not None and smax is not None and spin != smax:
        raise ValueError("Only one of spin or smax should be given")
    if spin is not None and smin is None:
        smin = spin
    if spin is not None and smax is None:
        smax = spin
    if spin is not None and spin != smin:
        raise ValueError("When spin is given, smin should be None or equal to spin")
    if spin is not None and spin != smax:
        raise ValueError("When spin is given, smax should be None or equal to spin")
    if smin is None and smax is not None:
        smin = -np.abs(smax)
    if smax is not None and smax is None:
        smin = np.abs(smin)
    if compact_spin is None:
        compact_spin = (smin is None and smax is None) or (smin == smax)
    lmin = 0 if lmin is None else lmin
    mmax = (lmax - 1) if mmax is None else max(min(mmax, lmax - 1), 1 - lmax)
    mmin = (1 - lmax) if mmin is None else max(min(mmin, lmax - 1), 1 - lmax)
    smax = (lmax - 1) if smax is None else max(min(smax, lmax - 1), 1 - lmax)
    smin = 1 - lmax if smin is None else max(min(smin, lmax - 1), 1 - lmax)
    return spin_legendre_labels(
        lmax=lmax,
        lmin=lmin,
        mmax=mmax,
        mmin=mmin,
        smin=smin,
        smax=smax,
        compact_spin=compact_spin if compact_spin is not None else True,
    )


def is_separable_spin(smin: int, smax: int, labels: Array) -> bool:
    """True if the labels can be separated."""
    if smin == smax:
        return True
    unicity = tf.unique_with_counts(labels[2])
    nspins = len(unicity.y)
    if len(labels[2]) % nspins != 0:
        return False
    indices = tf.reshape(unicity.idx, (nspins, -1))
    if tf.reduce_any(indices != tf.range(nspins)[:, None]):
        return False

    separated = tf.reshape(labels, (3, nspins, -1))
    if tf.reduce_any(separated[0, 0] != separated[0, 1:]):
        return False
    if tf.reduce_any(separated[1, 0] != separated[1, 1:]):
        return False
    return True


class Axis(str, Enum):
    """Names axes of interest.

    Example:

        >>> from tensossht.sampling import Axis
        >>> Axis("phi")
        <Axis.PHI: 'phi'>
        >>> Axis("phi") == "phi"
        True
        >>> Axis("theta") == "phi"
        False
        >>> Axis("theta") == Axis("theta")
        True

    """

    PHI: str = "phi"  # type: ignore
    THETA: str = "theta"  # type: ignore
    SPIN: str = "spin"  # type: ignore
    COEFF: str = "coeff"  # type: ignore


class ImageAxesBase(NamedTuple):
    """Avoids __classcell__ issues.

    NamedTuple does not pass ``__classcell__`` to ``type.__new__``, which means
    ``super`` cannot be used in python 3.8. We add a base class to avoid calling
    ``super`` directly.
    """

    phi: int
    theta: int
    spin: Optional[int] = None


class ImageAxes(ImageAxesBase):
    """Keeps track of the dimensions of an image tensor.

    Example:

        Images axes contain three components corresponding to the theta, phi and spin
        dimensions. Spin can be missing, in which case it is `None`.

        >>> from tensossht.sampling import ImageAxes, Axis
        >>> axes = ImageAxes(phi=-2, theta=-1, spin=1)
        >>> axes
        ImageAxes(phi=-2, theta=-1, spin=1)
        >>> axes[Axis.PHI]
        -2
        >>> axes["theta"]
        -1
        >>> axes[2]
        1
        >>> axes % 5
        ImageAxes(phi=3, theta=4, spin=1)

        One or more axis can be shifted to the end (e.g. most rapidly incrementing
        dimension in tensorflow):

        >>> axes.shift(5, Axis.PHI)
        ImageAxes(phi=-1, theta=-2, spin=1)
        >>> axes.shift(5, "spin")
        ImageAxes(phi=-3, theta=-2, spin=-1)
        >>> axes.shift(5, "spin", Axis.THETA)
        ImageAxes(phi=-3, theta=-1, spin=-2)

        Spin-less instances can still "shift" the spin axis, although nothing is done in
        that case. This makes it easier to implement spin and spin-less algorithms:

        >>> ImageAxes(phi=-2, theta=-1, spin=None).shift(5, Axis.PHI, Axis.SPIN)
        ImageAxes(phi=-1, theta=-2, spin=None)

        And a tensor can then be tranposed accordingly:

        >>> tensor = tf.zeros((2, 3, 4, 5, 6))
        >>> assert axes.transpose(tensor).shape == tensor.shape
        >>> assert axes.transpose(tensor, "spin").shape == (2, 4, 5, 6, 3)
        >>> assert axes.transpose(tensor, "spin", Axis.THETA).shape == (2, 4, 5, 3, 6)

        Optionally, the spin axis can be None, for single spin calculations:

        >>> axes = ImageAxes(phi=-2, theta=-1)
        >>> assert axes[Axis.SPIN] is None
        >>> assert axes.shift(3, Axis.PHI) == ImageAxes(theta=-2, phi=-1)

        In that case, shifting the spin axis is ignored:

        >>> assert axes.shift(3, Axis.SPIN) == axes
        >>> assert axes.shift(3, Axis.PHI, Axis.SPIN) == ImageAxes(theta=-2, phi=-1)

        Arbitrary permutations can be applied to the axes:

        >>> axes.permutate([1, 0, 3, 2, 4])
        ImageAxes(phi=-3, theta=-1, spin=None)

        It is also possible to figure out the permutation from one `ImageAxes` instance
        to another. The permutation does not change the order of the unnamed axes.


        >>> atstart = ImageAxes(phi=0, theta=1)
        >>> atend = ImageAxes(phi=-1, theta=-2)
        >>> atstart.permutation(atend, ndims=5)
        [2, 3, 4, 1, 0]
        >>> atend.permutation(atstart, ndims=6)
        [5, 4, 0, 1, 2, 3]

        >>> src = ImageAxes(phi=1, theta=-1, spin=-2)
        >>> dst = ImageAxes(phi=-1, spin=-3, theta=-2)
        >>> src.permutation(dst, ndims=5)
        [0, 2, 3, 4, 1]

        The transpose can be applied to a tensor as follows:

        >>> tensor = tf.zeros((2, 3, 4, 5, 6))
        >>> assert src.transpose(tensor, dst).shape == (2, 4, 5, 6, 3)

    """

    def __getitem__(self, index: Union[int, slice, Axis, str]):
        return ImageAxesBase.__getitem__(
            cast(Any, self), _axes_normalize_index(self, index)
        )

    def __mod__(self, ndims: int):
        return ImageAxes(*_axes_mod(self, ndims))

    def shift(self, ndims: int, *shifted: Union[str, Axis]):
        """Shift given axes to end."""
        return ImageAxes(**_axes_shift(self, ndims, *shifted))

    def transpose(
        self, tensor: Array, *shifted: Union[str, Axis, "ImageAxes"]
    ) -> TFArray:
        """Transpose tensor by shifting given axes to end."""
        return transpose(tensor, self, *shifted)

    def permutate(self, permutation: Sequence[int]):
        return ImageAxes(**_axes_permutate(self, permutation))

    def permutation(self, other: "ImageAxes", ndims: int):
        """Permutation taking this set of axes to input axes."""
        return _axes_permutation(ndims, self, other)


class HarmonicAxesBase(NamedTuple):
    """Avoids __classcell__ issues.

    NamedTuple does not pass ``__classcell__`` to ``type.__new__``, which means
    ``super`` cannot be used in python 3.8. We add a base class to avoid calling
    ``super`` directly.
    """

    coeff: int
    spin: Optional[int] = None


class HarmonicAxes(HarmonicAxesBase):
    """Keeps track of the dimensions of an spherical harmonic tensor.

    Example:

        Harmonics axes contain two components corresponding to the coefficient and spin
        dimensions. Spin can be missing, in which case it is `None`.

        >>> from tensossht.sampling import HarmonicAxes
        >>> axes = HarmonicAxes(coeff=-1, spin=-2)
        >>> axes
        HarmonicAxes(coeff=-1, spin=-2)
        >>> axes[Axis.COEFF]
        -1
        >>> axes["spin"]
        -2
        >>> axes[1]
        -2
        >>> axes % 5
        HarmonicAxes(coeff=4, spin=3)

        One or more axis can be shifted to the end (e.g. most rapidly incrementing
        dimension in tensorflow):

        >>> axes.shift(3, "coeff")
        HarmonicAxes(coeff=-1, spin=-2)
        >>> axes.shift(3, "spin")
        HarmonicAxes(coeff=-2, spin=-1)
        >>> axes.shift(3)
        HarmonicAxes(coeff=-1, spin=-2)
        >>> axes.shift(5, Axis.COEFF, "spin")
        HarmonicAxes(coeff=-2, spin=-1)

        And a tensor can then be tranposed accordingly:

        >>> tensor = tf.zeros((2, 3, 4, 5, 6))
        >>> assert axes.transpose(tensor).shape == tensor.shape
        >>> assert axes.transpose(tensor, "spin").shape == (2, 3, 4, 6, 5)
        >>> assert axes.transpose(tensor, "spin", Axis.COEFF).shape == (2, 3, 4, 5, 6)
        >>> assert axes.transpose(tensor, Axis.COEFF, "spin").shape == (2, 3, 4, 6, 5)

        It is also possible to compute the permutation to go from one axis ordering to
        another:

        >>> HarmonicAxes(coeff=0).permutation(HarmonicAxes(coeff=-1), ndims=3)
        [1, 2, 0]
        >>> HarmonicAxes(coeff=1, spin=-1).permutation(
        ...     HarmonicAxes(coeff=-1, spin=1), ndims=4
        ... )
        [0, 3, 2, 1]

    """

    def __getitem__(self, index: Union[int, slice, Axis, str]):
        return HarmonicAxesBase.__getitem__(
            cast(Any, self), _axes_normalize_index(self, index)
        )

    def __mod__(self, ndims: int):
        return HarmonicAxes(*_axes_mod(self, ndims))

    def shift(self, ndims: int, *shifted: Union[str, Axis]):
        """Shift given axes to end."""
        return HarmonicAxes(**_axes_shift(self, ndims, *shifted))

    def transpose(
        self, tensor: Array, *shifted: Union[str, Axis, "HarmonicAxes"]
    ) -> TFArray:
        """Transpose tensor by shifting given axes to end."""
        return transpose(tensor, self, *shifted)

    def permutate(self, permutation: Sequence[int]):
        return HarmonicAxes(**_axes_permutate(self, permutation))

    def permutation(self, other: "HarmonicAxes", ndims: int):
        """Permutation taking this set of axes to input axes."""
        return _axes_permutation(ndims, self, other)


def _axes_mod(axes: Iterable, ndims: int) -> Iterable:
    return ((item % ndims if item is not None else None) for item in axes)


def _axes_normalize_index(
    axes: Union[HarmonicAxes, ImageAxes], index
) -> Union[int, slice]:
    if isinstance(index, str):
        index = Axis(index.lower())
    if isinstance(index, Axis):
        for i, axis in enumerate(axes._fields):
            if index is Axis(axis):
                return i
        else:
            raise IndexError(f"Uknown index {index}")
    return index


def _axes_as_list(
    axes: Union[HarmonicAxes, ImageAxes], ndims: int
) -> List[Union[None, Axis]]:
    result: List[Union[None, Axis]] = [None] * ndims
    for field in axes._fields:
        index = cast(int, axes[field])
        if index is not None:
            assert result[index] is None
            result[index] = Axis(field)
    return result


def _axes_shift(
    axes: Union[HarmonicAxes, ImageAxes], ndims: int, *shifted_axes: Union[str, Axis]
):
    dims = _axes_as_list(axes, ndims)
    shifted: List[Union[None, Axis]] = [
        Axis(x) for x in shifted_axes if axes[x] is not None  # type: ignore
    ]
    reorder = [ax for ax in dims if ax not in shifted] + shifted
    return {
        k: i - ndims if Axis(k) in shifted or axes[k] < 0 else i  # type: ignore
        for i, k in enumerate(reorder)
        if k is not None
    }


def _axes_permutate(a: Union[HarmonicAxes, ImageAxes], permutation: Sequence[int]):
    ndims = len(permutation)
    axes = _axes_as_list(a, ndims)
    permutated = [axes[i] for i in permutation]
    return {
        v: i if a[v] > 0 else i - ndims  # type: ignore
        for i, v in enumerate(permutated)
        if v is not None
    }


def transpose(
    tensor: Array,
    axes: Union[ImageAxes, HarmonicAxes],
    *shifted_axes: Union[str, Axis, HarmonicAxes, ImageAxes],
) -> TFArray:
    """Transpose tensor so that given axes are pushed to the end."""
    if len(shifted_axes) == 0:
        return tensor
    if len(shifted_axes) > 1 and any(
        (isinstance(u, (HarmonicAxes, ImageAxes)) for u in shifted_axes)
    ):
        msg = "Input ought to be a single ImageAxes tuple or one or more Axis instances"
        raise ValueError(msg)
    if len(shifted_axes) > 1 or not isinstance(
        shifted_axes[0], (HarmonicAxes, ImageAxes)
    ):
        return transpose(
            tensor, axes, axes.shift(len(tensor.shape), *shifted_axes)  # type: ignore
        )
    return tf.transpose(
        tensor, _axes_permutation(len(tensor.shape), axes, shifted_axes[0])
    )


def _axes_permutation(
    ndims: int, src: Union[ImageAxes, HarmonicAxes], dst: Union[ImageAxes, HarmonicAxes]
) -> List[int]:
    from operator import itemgetter

    assert isinstance(src, ImageAxes) == isinstance(dst, ImageAxes)
    assert isinstance(src, HarmonicAxes) == isinstance(dst, HarmonicAxes)
    assert (src.spin is None) == (dst.spin is None)
    src = src % ndims
    dst = dst % ndims
    order = [
        u[0]
        for u in sorted(
            ((k, v) for k, v in dst._asdict().items() if v is not None),
            key=itemgetter(1),
        )
    ]
    permutation: List[int] = [i for i in range(ndims) if i not in src]
    for ax in order:
        permutation.insert(dst[ax], src[ax])  # type: ignore
    return permutation


def legendre_labels(
    lmax: int,
    lmin: Optional[int] = 0,
    mmax: Optional[int] = None,
    mmin: Optional[int] = 0,
) -> TFArray:
    r"""tensor with all (l, m) constrained by lmin, lmax and mmin, mmax.

    More specifically, we compute all values:

    .. math::

        \left\{
            (l, m);
            l \in [l_\text{min}, l_\text{max}[,
            m \in [m_\text{min}, m_\text{max}] \cap [-l, l]
        \right\}

    Generates a tensor with all ls and ms, as per requirements.
    ls are first and ms are second as illustrated below.

    Example:

        >>> from tensossht.sampling import legendre_labels
        >>> labels = legendre_labels(lmax=6, lmin=3, mmax=2, mmin=1)
        >>> labels
        <tf.Tensor: shape=(2, 6), dtype=int32, numpy=
        array([[3, 3, 4, 4, 5, 5],
               [1, 2, 1, 2, 1, 2]], dtype=int32)>
        >>> l, m = labels
        >>> l.numpy()
        array([3, 3, 4, 4, 5, 5], dtype=int32)

    """
    if mmin is None:
        mmin = -lmax
    if mmax is None:
        mmax = lmax
    if lmin is None:
        lmin = 0
    if lmin > lmax:
        raise ValueError(f"lmin > lmax ({lmin} > {lmax}")
    if mmin > mmax:
        raise ValueError(f"mmin > mmax ({mmin} > {mmax}")
    ls = tf.concat(
        [tf.fill((min(l, mmax) + 1 - max(-l, mmin),), l) for l in range(lmin, lmax)], 0
    )
    ms = tf.concat(
        [tf.range(max(-l, mmin), min(l, mmax) + 1) for l in range(lmin, lmax)], 0
    )
    return tf.concat([tf.expand_dims(ls, 0), tf.expand_dims(ms, 0)], axis=0)


def spin_legendre_labels(
    lmax: int,
    lmin: int = 0,
    mmax: Optional[int] = None,
    mmin: Optional[int] = 0,
    smax: Optional[int] = None,
    smin: Optional[int] = 0,
    dtype: Union[tf.DType, np.dtype, str] = tf.int32,
    compact_spin: bool = True,
) -> TFArray:
    r"""tensor with all (l, m, s) constrained by lmin, lmax and mmin, mmax, smin, smax.

    More specifically, we compute all values:

    .. math::

        \left\{
            (l, m, s);
            s \in [s_\text{min}, s_\text{max}]
            l \in [l_\text{min}, l_\text{max}[,\ l \geq |s|,
            m \in [m_\text{min}, m_\text{max}],\ -l \geq m \geq l
        \right\}

    Generates a tensor with all ls and ms, as per requirements.
    All pairs ``(l, m)`` for a given ``s`` are contiguous, e.g. ``s` is the outermost
    index. ``m`` is the innermost index, e.g. the most rapidly changing. This setup
    implies we could expand the labels into a 2-dimensional ragged tensor ``s`` vs ``(l,
    m)``.

    If `compact_spin` is ``True`` then the labels are arranged such that memory is
    optimized. If it false, then the tensor can be reshaped so that the spins are in a
    separate dimension.

    Example:

        The followin illustrates a compact label representation.

        >>> from tensossht import spin_legendre_labels
        >>> labels = spin_legendre_labels(lmax=3, smin=-1, smax=1)
        >>> labels
        <tf.Tensor: shape=(3, 16), dtype=int32, numpy=
        array([[ 1,  1,  2,  2,  2,  0,  1,  1,  2,  2,  2,  1,  1,  2,  2,  2],
               [ 0,  1,  0,  1,  2,  0,  0,  1,  0,  1,  2,  0,  1,  0,  1,  2],
               [-1, -1, -1, -1, -1,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1]],
              dtype=int32)>
        >>> l, m, s = labels
        >>> l.numpy()
        array([1, 1, 2, 2, 2, 0, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2], dtype=int32)

        However, a less compact representation is available:

        >>> labels = spin_legendre_labels(lmax=3, smin=-1, smax=1, compact_spin=False)
        >>> tf.reshape(labels, (3, 3, -1))
        <tf.Tensor: shape=(3, 3, 6), dtype=int32, numpy=
        array([[[ 0,  1,  1,  2,  2,  2],
                [ 0,  1,  1,  2,  2,  2],
                [ 0,  1,  1,  2,  2,  2]],
        <BLANKLINE>
               [[ 0,  0,  1,  0,  1,  2],
                [ 0,  0,  1,  0,  1,  2],
                [ 0,  0,  1,  0,  1,  2]],
        <BLANKLINE>
               [[-1, -1, -1, -1, -1, -1],
                [ 0,  0,  0,  0,  0,  0],
                [ 1,  1,  1,  1,  1,  1]]], dtype=int32)>

    """
    if mmin is None:
        mmin = -lmax
    if mmax is None:
        mmax = lmax
    if smax is None:
        smax = lmax
    if smin is None:
        smin = -lmax
    if lmax < 0:
        raise ValueError(f"lmax ({lmax}) < 0")
    if lmin > lmax:
        raise ValueError(f"lmin > lmax ({lmin} > {lmax}")
    if mmin > mmax:
        raise ValueError(f"mmin > mmax ({mmin} > {mmax}")
    if smin > smax:
        raise ValueError(f"smin > smax ({smin} > {smax}")
    return tf.roll(
        tf.transpose(
            tf.constant(
                [
                    (s, order, m)
                    for s in range(smin, smax + 1)
                    for order in range(
                        max(abs(s), lmin) if compact_spin else lmin, lmax
                    )
                    for m in range(max(-order, mmin), min(order, mmax) + 1)
                ],
                dtype=dtype,
            )
        ),
        shift=-1,
        axis=0,
    )


def wignerd_labels(
    lmax: int,
    lmin: int = 0,
    mmax: Optional[int] = None,
    mmin: Optional[int] = None,
    mpmin: Optional[int] = None,
    mpmax: Optional[int] = None,
) -> TFArray:
    r"""tensor with all (l, m, m') constrained by the input arguments

    More specifically, we compute all values:

    .. math::

        \left\{
            (l, m, m');
            l \in [l_\text{min}, l_\text{max}[,
            m \in [m_\text{min}, m_\text{max}] \cap [-l, l]
            m' \in [m'_\text{min}, m'_\text{max}] \cap [-l, l]
        \right\}

    Generates a tensor with all :math:`l, m, m'` as per requirements.  The first row
    corresponds to :math:`l`, the second to :math:`m`, and the third to :math:`m'`.

    Example:

        >>> from tensossht import wignerd_labels
        >>> labels = wignerd_labels(lmax=6, lmin=3, mmax=2, mmin=-1, mpmax=1, mpmin=-2)
        >>> labels
        <tf.Tensor: shape=(3, 48), dtype=int32, numpy=
        array([[ 3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,
                 4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,
                 5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5],
               [-1, -1, -1, -1,  0,  0,  0,  0,  1,  1,  1,  1,  2,  2,  2,  2,
                -1, -1, -1, -1,  0,  0,  0,  0,  1,  1,  1,  1,  2,  2,  2,  2,
                -1, -1, -1, -1,  0,  0,  0,  0,  1,  1,  1,  1,  2,  2,  2,  2],
               [-2, -1,  0,  1, -2, -1,  0,  1, -2, -1,  0,  1, -2, -1,  0,  1,
                -2, -1,  0,  1, -2, -1,  0,  1, -2, -1,  0,  1, -2, -1,  0,  1,
                -2, -1,  0,  1, -2, -1,  0,  1, -2, -1,  0,  1, -2, -1,  0,  1]],
              dtype=int32)>

    """

    if mmin is None:
        mmin = -lmax
    if mmax is None:
        mmax = lmax
    if lmin > lmax:
        raise ValueError(f"lmin > lmax ({lmin} > {lmax}")
    if mmin > mmax:
        raise ValueError(f"mmin > mmax ({mmin} > {mmax}")
    if mpmin is None:
        mpmin = mmin
    if mpmax is None:
        mpmax = mmax

    ls = tf.concat(
        [
            tf.fill(
                (
                    (min(l, mmax) + 1 - max(-l, mmin))
                    * (min(l, mpmax) + 1 - max(-l, mpmin)),
                ),
                l,
            )
            for l in range(lmin, lmax)
        ],
        0,
    )
    ms = tf.concat(
        [
            tf.repeat(
                tf.range(max(-l, mmin), min(l, mmax) + 1),
                (min(l, mpmax) + 1 - max(-l, mpmin)),
                0,
            )
            for l in range(lmin, lmax)
        ],
        0,
    )
    mps = tf.concat(
        [
            tf.tile(
                tf.range(max(-l, mpmin), min(l, mpmax) + 1),
                (min(l, mmax) + 1 - max(-l, mmin),),
            )
            for l in range(lmin, lmax)
        ],
        0,
    )
    return tf.concat(
        [tf.expand_dims(ls, 0), tf.expand_dims(ms, 0), tf.expand_dims(mps, 0)], axis=0
    )


def symmetric_labels(
    labels: Array, dtype: Union[str, np.dtype, tf.DType] = tf.int32
) -> Tuple[TFArray, TFArray]:
    """Symmetrize wigner-d (l, m, m') labels so m >= m' >= 0.

    Returns a tuple with the symetrized labels and the sign factor.

    Example:

        First we create the labels:

        >>> from tensossht import wignerd_labels
        >>> from tensossht.sampling import symmetric_labels
        >>> labels = wignerd_labels(8)
        >>> symlabs, factors = symmetric_labels(labels)

        The we can verify the labels have been symmtrized:

        >>> assert tf.reduce_all(symlabs[1] >= symlabs[-1])
        >>> assert tf.reduce_all(symlabs[-1] >= 0)

        We can check that the wigner-ds are equal to a factor, using the naive
        multi-precision implementation:

        >>> from pytest import approx
        >>> from tensossht.specialfunctions.naive import wignerd
        >>> for i in range(labels.shape[1]):
        ...     expected = wignerd(*labels[:, i].numpy())
        ...     actual = factors[i].numpy() * wignerd(*symlabs[:, i].numpy())
        ...     assert actual == approx(expected)

    """
    ms = tf.where(tf.abs(labels[1]) >= tf.abs(labels[-1]), labels[1:], -labels[2:0:-1])
    factors = tf.where(
        tf.logical_and(ms[0] < 0, (labels[0] - ms[1]) % 2 == 1)
        != tf.logical_and(ms[1] < 0, (labels[0] - ms[0]) % 2 == 1),
        tf.constant(-1, dtype=dtype),
        tf.constant(1, dtype=dtype),
    )
    labels = tf.concat((labels[0:1], tf.abs(ms)), axis=0)
    return labels, factors
