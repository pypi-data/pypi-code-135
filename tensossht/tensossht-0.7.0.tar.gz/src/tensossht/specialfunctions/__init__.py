"""
=================
Special Functions
=================

This module contains different approach to computing the  Wigner-d matrices, legendre
polynomials and spherical harmonics, as well as some helper functions.

.. automodule:: tensossht.specialfunctions.risbo

.. automodule:: tensossht.specialfunctions.kostelec

.. automodule:: tensossht.specialfunctions.trapani

.. automodule:: tensossht.specialfunctions.naive

Other functions and data-structures
===================================

.. autofunction :: tensossht.specialfunctions.legendre
.. autofunction :: tensossht.specialfunctions.spherical_harmonics
.. autofunction :: tensossht.specialfunctions.to_matrix_coefficients
.. autofunction :: tensossht.specialfunctions.to_compressed_coefficients
.. autofunction :: tensossht.specialfunctions.legendre_lsum

.. autoclass :: tensossht.specialfunctions.Methods
"""
from enum import Enum, auto, unique
from typing import List, Optional, Tuple, Union

import numpy as np
import tensorflow as tf

from tensossht.specialfunctions import kostelec, naive, risbo, trapani

__all__ = [
    "Methods",
    "legendre",
    "spherical_harmonics",
    "legendre_lsum",
    "to_matrix_coefficients",
    "to_compressed_coefficients",
    "risbo",
    "kostelec",
    "naive",
    "trapani",
]


@unique
class Methods(Enum):
    NAIVE = auto()
    """Brute-force or hard-coded implementations."""
    NUMERICAL_RECIPES = auto()
    """Recurrence from numerical recipes."""
    KOSTELEC = auto()
    """Recurrence from Kostelec and Rockmore (2008)."""
    TRAPANI = auto()
    """Recurrence from Trapani and Navaza (2006)."""


def legendre(
    beta: Union[float, List[float], tf.Tensor],
    *args,
    method: Methods = Methods.KOSTELEC,
    **kwargs,
) -> tf.Tensor:
    """Legendre polynomial using one of several methods or recurrence.

    Argument and keywords are passed on to the legendre function from the relevant
    module.

    Example:

        >>> from tensossht.specialfunctions import legendre, Methods
        >>> legpol = legendre(beta=0.4, lmax=4, method=Methods.KOSTELEC)
        >>> legpol.numpy().round(4)
        array([ 1.    ,  0.9211, -0.2754,  0.7725, -0.4393,  0.0929,  0.5719,
               -0.5466,  0.1913, -0.033 ], dtype=float32)

    """
    from tensossht.specialfunctions import kostelec, naive, numericalrecipes

    beta = tf.convert_to_tensor(beta, name="beta")
    if method is Methods.NAIVE:
        return naive.legendre(tf.cos(beta), *args, **kwargs)
    if method is Methods.NUMERICAL_RECIPES:
        return numericalrecipes.legendre(tf.cos(beta), *args, **kwargs)
    if method is Methods.KOSTELEC:
        return kostelec.legendre(beta, *args, **kwargs)
    if method is Methods.TRAPANI:
        msg = "Legendre was not implemented using the Trapani scheme."
        raise NotImplementedError(msg)


def spherical_harmonics(
    theta: tf.Tensor,
    phi: tf.Tensor,
    lmax: Optional[int] = None,
    lmin: int = 0,
    mmin: Optional[int] = None,
    mmax: Optional[int] = None,
    labels: Optional[Union[np.ndarray, tf.Tensor]] = None,
    method: Methods = Methods.KOSTELEC,
) -> tf.Tensor:
    r"""Spherical harmonics as obtained from the legendre polynomials:

    .. math::

        Y_{lm}(\theta, \phi) =
            \sqrt{\frac{2l + 1}{4\pi}\frac{(l - m)!}{(l + m)!}}
            P_l^m(\cos{\theta})
            e^{\imath m\phi}

    Example:

        We can compute the spherical harmonics over a given sampling grid:

        >>> from tensossht import sampling, spherical_harmonics
        >>> lmax = 5
        >>> grid = sampling.equiangular(lmax=lmax, dtype=tf.float64).numpy()
        >>> theta, phi = grid[0].flatten(), grid[1].flatten()
        >>> sph = spherical_harmonics(theta, phi, lmax=lmax)
        >>> sph.ndim
        2

        The first dimension corresponds to the number of points on the grid:

        >>> assert sph.shape[0] == len(theta)

        The second dimension corresponds to each spherical harmonic, up to `lmax=5` in
        our example. We reconstruct the matrix of (l, m) labels below:

        >>> from tensossht import legendre_labels
        >>> labels = legendre_labels(lmax=lmax, mmin=None)
        >>> assert sph.shape[1] == labels.shape[1]

        We can verify that first harmonic ``(l=0, m=0)`` is equal to
        :math:`\frac{1}{2\sqrt{\pi}}`:

        >>> from pytest import approx
        >>> tuple(labels[:, 0].numpy())
        (0, 0)
        >>> assert sph[:, 0].numpy() == approx(0.5 / np.sqrt(np.pi))

        More generally, we can compare to the hard-coded spherical harmonics from
        :py:mod:`tensossht.specialfunctions.naive`:

        >>> from tensossht.specialfunctions import naive
        >>> for i, (l, m) in enumerate(labels[:15].numpy().T):
        ...     expected = [
        ...         naive.spherical_harmonics(t, p, l, m)
        ...         for t, p in zip(theta, phi)
        ...     ]
        ...     assert sph[:, i].numpy() == approx(expected)

    """
    from tensossht.sampling import legendre_labels

    if labels is None and lmax is None:
        raise ValueError("At least one of lmax or labels is required on input")
    elif labels is not None and lmax is not None and lmax != tf.reduce_max(labels):
        raise ValueError("Only one lmax or labels should be given on input")
    elif lmax is not None:
        labels = legendre_labels(lmax=lmax, lmin=lmin, mmin=mmin, mmax=mmax)
    else:
        labels = tf.convert_to_tensor(labels)
    assert labels is not None
    legpol = legendre(theta, labels=labels, scaled=True, method=method)
    factor = tf.sqrt(tf.cast(2 * labels[0] + 1, dtype=legpol.dtype) / (4 * np.pi))
    expphi = tf.exp(
        tf.complex(
            tf.zeros(1, dtype=phi.dtype),
            tf.cast(labels[1], dtype=phi.dtype) * phi[..., None],
        )
    )

    return tf.complex(factor * legpol, tf.zeros(1, dtype=theta.dtype)) * expphi


def normalize_inputs(
    l: Union[tf.Tensor, np.ndarray, List],
    m: Union[tf.Tensor, np.ndarray, List],
    x: Union[tf.Tensor, np.ndarray, List],
) -> Tuple[tf.Tensor, tf.Tensor, tf.Tensor]:
    degree: tf.Tensor = tf.convert_to_tensor(value=l, name="degree")
    order: tf.Tensor = tf.convert_to_tensor(value=m, name="order")
    values: tf.Tensor = tf.convert_to_tensor(value=x, name="x")
    return degree, order, values


@tf.function
def legendre_lsum(
    data: tf.Tensor,
    lmax: int,
    lmin: int = 0,
    mmax: Optional[int] = None,
    mmin: Optional[int] = 0,
    axis: Union[int, tf.Tensor] = tf.constant(0),
    constant_values=0,
) -> tf.Tensor:
    """Sums coefficients over L.

    Assumes the data is in the same order as given by :py:func:`legendre_labels` and
    performs a reduction over l.


    Example:

        The point is that the data for any given all only contains elements satisfying
        the conditions :math:`-l \\leq m \\leq l` and :math:`m_\\mathrm{min} \\leq m
        \\leq m_\\mathrm{max}`. Elements outside this range default to zero.

        >>> from tensossht import legendre_labels
        >>> from tensossht.specialfunctions import legendre_lsum
        >>> lmax, lmin, mmax, mmin = 8, 2, 4, -3
        >>> labels = legendre_labels(lmax=lmax, lmin=lmin, mmax=mmax, mmin=mmin)
        >>> legendre_lsum(labels[0], lmax=lmax, lmin=lmin, mmax=mmax, mmin=mmin).numpy()
        array([25, 27, 27, 27, 27, 27, 25, 22], dtype=int32)

        Above, the first and last two items are those for which some coefficients
        defaulted to zero.

        The summation works for any number of dimensions, as long as the :math:`(l, m)`
        axis is provided (defaults to zero).

        >>> repeats = tf.tile(labels[0][None, :], (2, 1))
        >>> legendre_lsum(
        ...     repeats, lmax=lmax, lmin=lmin, mmax=mmax, mmin=mmin, axis=1
        ... ).numpy()
        array([[25, 27, 27, 27, 27, 27, 25, 22],
               [25, 27, 27, 27, 27, 27, 25, 22]], dtype=int32)
        >>> legendre_lsum(
        ...     tf.transpose(repeats),
        ...     lmax=lmax,
        ...     lmin=lmin,
        ...     mmax=mmax,
        ...     mmin=mmin,
        ...     axis=0
        ... ).numpy()
        array([[25, 25],
               [27, 27],
               [27, 27],
               [27, 27],
               [27, 27],
               [27, 27],
               [25, 25],
               [22, 22]], dtype=int32)

    """
    if mmax is None:
        mmax = lmax
    if mmin is None:
        mmin = -lmax

    lower = np.array([max(min(-l, mmax), mmin) for l in range(lmin, lmax)])
    upper = np.array([max(min(l, mmax), mmin) for l in range(lmin, lmax)])
    ends = np.cumsum(upper) + np.arange(1, len(upper) + 1) - np.cumsum(lower)
    starts = np.concatenate((np.array([0]), ends[:-1], np.array([0])))

    m0 = np.min(lower)
    m1 = np.max(upper)

    ndim = tf.rank(data)
    axis = axis % ndim
    prepad = tf.zeros((axis, 2), dtype=tf.int32)
    postpad = tf.zeros((ndim - 1 - axis, 2), dtype=tf.int32)

    def iteration(i):
        padding = tf.concat((prepad, [[lower[i] - m0, m1 - upper[i]]], postpad), 0)
        summand = tf.gather(data, range(starts[i], ends[i]), axis=axis)
        return tf.pad(summand, padding, constant_values=constant_values)

    result = iteration(0)
    for i in range(1, lmax - lmin):
        result += iteration(i)

    return result


@tf.function
def to_matrix_coefficients(
    coefficients: tf.Tensor,
    lmax: int,
    lmin: int = 0,
    mmax: Optional[int] = None,
    mmin: Optional[int] = None,
    fill_value: Union[int, float, complex, tf.Tensor, tf.Variable] = 0,
    coeff_dim: int = 0,
    l_dim: int = 0,
    m_dim: int = 1,
) -> tf.Tensor:
    """Converts compressed coefficients to matrix form.

    Example:

        We can convert the labels themselves from compressed to matrix form:

        >>> from tensossht import legendre_labels
        >>> lmax, lmin, mmax, mmin = 4, 1, 3, -2
        >>> labels = legendre_labels(lmax=lmax, lmin=lmin, mmax=mmax, mmin=mmin)
        >>> labels
        <tf.Tensor: shape=(2, 14), dtype=int32, numpy=
        array([[ 1,  1,  1,  2,  2,  2,  2,  2,  3,  3,  3,  3,  3,  3],
               [-1,  0,  1, -2, -1,  0,  1,  2, -2, -1,  0,  1,  2,  3]],
              dtype=int32)>

        The array above uses memory optimally in that each element is used. However, it
        can be difficult to address directly an element of a given degree and order. The
        conversion provides a matrix form with simpler addressing at the cost of greater
        memory usages.

        >>> from tensossht import to_matrix_coefficients
        >>> to_matrix_coefficients(
        ...     labels, lmax, lmin, mmax, mmin,
        ...     coeff_dim=-1, fill_value=100, l_dim=-2, m_dim=-1,
        ... )
        <tf.Tensor: shape=(2, 3, 6), dtype=int32, numpy=
        array([[[100,   1,   1,   1, 100, 100],
                [  2,   2,   2,   2,   2, 100],
                [  3,   3,   3,   3,   3,   3]],
        <BLANKLINE>
               [[100,  -1,   0,   1, 100, 100],
                [ -2,  -1,   0,   1,   2, 100],
                [ -2,  -1,   0,   1,   2,   3]]], dtype=int32)>

        The l's vary across columns, whereas the m's varie across rows. The two indices
        are now separate dimensions.
    """
    assert mmax is None or mmax >= 0
    assert mmin is None or mmin <= 0

    ndim = len(tf.shape(coefficients))
    coeff_dim %= ndim
    if coeff_dim != 0:
        coefficients = tf.transpose(
            coefficients,
            [coeff_dim] + list(range(coeff_dim)) + list(range(coeff_dim + 1, ndim)),
        )

    mmax = (lmax - 1) if mmax is None else max(min(mmax, lmax - 1), 1 - lmax)
    mmin = (1 - lmax) if mmin is None else max(min(mmin, lmax - 1), 1 - lmax)
    if mmin is None:
        mmin = -lmax

    ls = tf.range(lmin, lmax)[:, None]
    l_ind = tf.where(
        ls <= mmax,
        (ls * (ls + 1)) // 2,
        (mmax * (mmax + 1)) // 2 + (mmax + 1) * (ls - mmax),
    ) + tf.where(
        ls <= -mmin, (ls * (ls - 1)) // 2, (mmin * (mmin + 1)) // 2 - mmin * (ls + mmin)
    )
    m_ind = tf.range(mmin, mmax + 1)[None, :]
    valid = tf.logical_and(ls >= m_ind, m_ind >= -ls)
    indices = tf.where(
        valid, l_ind - l_ind[0, 0] + tf.where(mmin <= -ls, m_ind + ls, m_ind - mmin), 0
    )
    result = tf.where(
        tf.reshape(valid, [-1] + [1] * (ndim - 1)),
        tf.gather(coefficients, tf.reshape(indices, (-1,))),
        fill_value,
    )
    result = tf.reshape(
        result, tf.concat((tf.shape(indices), tf.shape(result)[1:]), axis=0)
    )

    l_dim %= ndim + 1
    m_dim %= ndim + 1
    if l_dim != 0 or m_dim != 1:
        p = list(range(ndim + 1))
        p[0], p[l_dim] = p[l_dim], p[0]
        p[1 if l_dim != 1 else 0], p[m_dim] = p[m_dim], p[1 if l_dim != 1 else 0]
        result = tf.transpose(result, p)
    return result


@tf.function
def to_compressed_coefficients(
    matrix: tf.Tensor,
    lmax: Optional[int] = None,
    lmin: Optional[int] = None,
    mmax: Optional[int] = None,
    mmin: Optional[int] = None,
    labels: Optional[tf.Tensor] = None,
    l_dim: int = 0,
    m_dim: int = 1,
    coeff_dim: int = 0,
) -> tf.Tensor:
    """Converts compressed coefficients to matrix form.

    Example:

        We can convert the labels themselves from matrix to compressed form. The matrix
        below is 2 by l by m. The matrix contains unnecessary extra elements,
        initialized for show to 100 below. However, it is easy to address a specific
        :math:`(l, m)`. On the other hand, the compressed form is optimal in terms of
        memory consumption. However, addressing a given :math:`(l, m)` is not trivial.

        >>> from tensossht import to_compressed_coefficients, legendre_labels
        >>> lmax, lmin, mmax, mmin = 4, 1, 3, -2
        >>> matrix = tf.constant(
        ...     # order l
        ...     [[[100,   1,   1,   1, 100, 100],
        ...       [  2,   2,   2,   2,   2, 100],
        ...       [  3,   3,   3,   3,   3,   3]],
        ...     # degree m
        ...      [[100,  -1,   0,   1, 100, 100],
        ...       [ -2,  -1,   0,   1,   2, 100],
        ...       [ -2,  -1,   0,   1,   2,   3]]]
        ... )
        >>> compressed = to_compressed_coefficients(
        ...     matrix, lmax, lmin, mmax, mmin, coeff_dim=-1, l_dim=-2, m_dim=-1
        ... )
        >>> labels = legendre_labels(lmax=lmax, lmin=lmin, mmax=mmax, mmin=mmin)
        >>> assert (compressed == labels).numpy().all()

    """
    from tensossht.sampling import legendre_labels

    assert mmax is None or mmax >= 0
    assert mmin is None or mmin <= 0
    if labels is None and lmax is None:
        raise ValueError("One of labels or lmax must be provided.")
    if labels is None:
        assert lmax is not None
        labels = legendre_labels(lmax=lmax, lmin=lmin, mmax=mmax, mmin=mmin)
        if lmin is None:
            lmin = 0
        if mmin is None:
            mmin = -lmax
        if mmax is None:
            mmax = lmax
    assert labels is not None
    if lmax is None:
        lmax = int(tf.reduce_max(labels[0]))
    if mmax is None:
        mmax = int(tf.reduce_max(labels[1]))
    if lmin is None:
        lmin = int(tf.reduce_min(labels[0]))
    if mmin is None:
        mmin = int(tf.reduce_min(labels[1]))

    ndim = len(tf.shape(matrix))
    l_dim %= ndim
    m_dim %= ndim
    if l_dim != 0 or m_dim != 1:
        matrix = tf.transpose(
            matrix,
            [l_dim, m_dim] + [i for i in range(ndim) if i != l_dim and i != m_dim],
        )

    indices = tf.concat(((labels[0] - lmin)[:, None], (labels[1] - mmin)[:, None]), 1)
    result = tf.gather_nd(matrix, indices)

    coeff_dim %= ndim - 1
    if coeff_dim != 0:
        perm = list(range(ndim - 1))
        perm[0], perm[coeff_dim] = perm[coeff_dim], perm[0]
        result = tf.transpose(result, perm)
    return result
