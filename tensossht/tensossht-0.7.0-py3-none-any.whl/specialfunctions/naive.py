"""
Naive brute-force implementations
=================================

These are straightforward implementation of the special functions. They are only
useful for testing and as definitions.

API
---

.. autofunction:: tensossht.specialfunctions.naive.wignerd
.. autofunction:: tensossht.specialfunctions.naive.legendre
.. autofunction:: tensossht.specialfunctions.naive.spherical_harmonics
.. autofunction:: tensossht.specialfunctions.naive.spin_spherical_harmonics
.. autofunction:: tensossht.specialfunctions.naive._spin_spherical_harmonics
"""
from typing import Optional, Sequence, Union

import numpy as np
import tensorflow as tf


def wignerd(
    l: int,
    m1: Union[None, Sequence, int] = None,
    m2: Union[None, Sequence, int] = None,
    beta: Optional[float] = None,
    precision: Optional[int] = None,
) -> np.ndarray:
    """Straight-forward Wigner d-matrix implementation.

    Relies on arbirtrary precision floating points for numerical stability. Safe but
    slow.

    .. math::

        d_{mm'}^l(\\beta) =
            \\sqrt{!(l + m)!(l - m)!(l + m')!(l - m')}
            \\sum_s
            \\frac{
                (-1)^{m - m' + s}
                \\left(\\cos\\frac{\\beta}{2}\\right)^{2(l - s) + m' - m}
                \\left(\\sin\\frac{\\beta}{2}\\right)^{2s + m - m'}
            }{!(l - m - s)!(l + m' - s)!(s + m - m')!k}

    With :math:`s` such that the terms in the factorial are positive or null:

    .. math::

        l - m &\\geq s

        l + m' &\\geq s

        s &\\geq 0

        s &\\geq m' - m
    """
    from mpmath import cos, factorial, mp, pi, sin, sqrt
    from numpy import array

    if m1 is None:
        m1 = range(-l, l + 1)
    if m2 is None:
        m2 = range(-l, l + 1)

    if precision is not None:
        old = mp.dps
        try:
            mp.dps = precision
            return wignerd(l, m1, m2, beta, None)
        finally:
            mp.dps = old

    if isinstance(m1, Sequence) and isinstance(m2, Sequence):
        return array([[wignerd(l, i, j, beta, precision) for j in m2] for i in m1])
    elif isinstance(m1, Sequence) and not isinstance(m2, Sequence):
        return array([wignerd(l, i, m2, beta, precision) for i in m1])
    elif isinstance(m2, Sequence):
        return array([wignerd(l, m1, j, beta, precision) for j in m2])

    assert not isinstance(m1, Sequence)
    assert not isinstance(m2, Sequence)

    if m1 < -l or m1 > l or m2 < -l or m2 > l:
        return np.array(0)

    if beta is None:
        beta = pi / 2
    assert beta is not None

    result = 0
    numerator = sqrt(
        factorial(l + m1) * factorial(l - m1) * factorial(l + m2) * factorial(l - m2)
    )
    for k in range(max(0, m2 - m1), min(l - m1, l + m2) + 1):
        denominator = (
            factorial(l - m1 - k)
            * factorial(l + m2 - k)
            * factorial(k + m1 - m2)
            * factorial(k)
        )
        factor = (1 if (k + m1 - m2) % 2 == 0 else -1) * numerator / denominator
        result += (
            factor
            * cos(beta / 2) ** (2 * l - 2 * k + m2 - m1)
            * sin(beta / 2) ** (2 * k + m1 - m2)
        )
    return result


def legendre(l: int, m: int, x: float) -> float:
    """Associated legendre functions up to l = 4 and  m = 4.

    As given by `wikipedia`__.

    __ : https://en.wikipedia.org/wiki/Associated_Legendre_polynomials
    """
    from math import sqrt

    if (l, m) == (0, 0):
        return 1
    elif (l, m) == (1, 0):
        return x
    elif (l, m) == (1, -1):
        return -legendre(l, -m, x) / 2
    elif (l, m) == (1, 1):
        return -sqrt(1 - x * x)
    elif (l, m) == (2, -2):
        return legendre(l, -m, x) / 24
    elif (l, m) == (2, -1):
        return -legendre(l, -m, x) / 6
    elif (l, m) == (2, 0):
        return (3 * x * x - 1) / 2
    elif (l, m) == (2, 1):
        return -3 * x * sqrt(1 - x * x)
    elif (l, m) == (2, 2):
        return 3 * (1 - x * x)
    elif (l, m) == (3, -3):
        return -legendre(l, -m, x) / 720
    elif (l, m) == (3, -2):
        return legendre(l, -m, x) / 120
    elif (l, m) == (3, -1):
        return -legendre(l, -m, x) / 12
    elif (l, m) == (3, 0):
        return (5 * x * x * x - 3 * x) / 2
    elif (l, m) == (3, 1):
        return -(5 * x * x - 1) * sqrt(1 - x * x) * 3 / 2
    elif (l, m) == (3, 2):
        return 15 * x * (1 - x * x)
    elif (l, m) == (3, 3):
        z = 1 - x * x
        return -15 * z * sqrt(z)
    elif (l, m) == (4, -4):
        return legendre(l, -m, x) / 40320
    elif (l, m) == (4, -3):
        return -legendre(l, -m, x) / 5040
    elif (l, m) == (4, -2):
        return legendre(l, -m, x) / 360
    elif (l, m) == (4, -1):
        return -legendre(l, -m, x) / 20
    elif (l, m) == (4, 0):
        z = x * x
        return (35 * z * z - 30 * z + 3) / 8
    elif (l, m) == (4, 1):
        return -(7 * x * x * x - 3 * x) * sqrt(1 - x * x) * 5 / 2
    elif (l, m) == (4, 2):
        return (7 * x * x - 1) * (1 - x * x) * 15 / 2
    elif (l, m) == (4, 3):
        z = 1 - x * x
        return -105 * x * z * sqrt(z)
    elif (l, m) == (4, 4):
        z = 1 - x * x
        return 105 * z * z
    raise ValueError("Expected 0 <= l <= 4 and -l <= m <= l.")


def spherical_harmonics(theta: float, phi: float, l: int, m: int) -> float:
    """Spherical harmonics up to :math:`(l=4, m=4)`.

    Example:

        >>> from tensossht.specialfunctions.naive import spherical_harmonics
        >>> np.round(spherical_harmonics(np.pi / 3, np.pi / 2, 0, 0), 8)
        (0.28209479+0j)
        >>> np.round(spherical_harmonics(np.pi / 3, np.pi / 2, 1, 0), 8)
        (0.24430126+0j)
        >>> np.round(spherical_harmonics(np.pi / 3, np.pi / 2, 1, 1), 8)
        (-0-0.29920671j)
        >>> np.round(spherical_harmonics(np.pi / 3, np.pi / 2, 2, 0), 8)
        (-0.07884789+0j)
        >>> np.round(spherical_harmonics(np.pi / 3, np.pi / 2, 2, 1), 8)
        (-0-0.33452327j)

    """
    from scipy.special import gamma

    return (
        legendre(l, m, np.cos(theta))
        * np.sqrt((2 * l + 1) / (4 * np.pi) * gamma(l - m + 1) / gamma(l + m + 1))
        * np.exp(1j * m * phi)
    )


def spin_spherical_harmonics(
    theta: tf.Tensor,
    phi: tf.Tensor,
    lmax: int,
    lmin: int = 0,
    mmax: Optional[int] = None,
    mmin: Optional[int] = None,
    smax: Optional[int] = None,
    smin: Optional[int] = None,
    spin: Optional[int] = None,
    precision: Optional[int] = None,
    compact_spin: Optional[bool] = None,
) -> tf.Tensor:
    """Spin-weighted spherical harmonics the naive way.

    Examples:

        >>> from pytest import approx
        >>> from tensossht import spherical_harmonics
        >>> from tensossht.specialfunctions import naive
        >>> theta = tf.range(0, 1, 0.2)
        >>> phi = tf.range(0, 1, 0.2)
        >>> expected = spherical_harmonics(theta, phi, lmax=3)
        >>> actual = naive.spin_spherical_harmonics(theta, phi, lmax=3, smax=0, smin=0)
        >>> assert tf.reduce_all(tf.math.abs(actual - expected) < 1e-6)

    """
    from tensossht.sampling import harmonic_sampling_scheme

    hsampling = harmonic_sampling_scheme(
        lmax, lmin, mmax, mmin, smax, smin, spin=spin, compact_spin=compact_spin
    )
    assert theta.shape == phi.shape
    flat_theta = tf.reshape(theta, (-1,))
    flat_phi = tf.reshape(phi, (-1,))
    result = [
        [
            complex(
                _spin_spherical_harmonics(
                    float(flat_theta[i]), float(flat_phi[i]), l, m, s
                )
            )
            for l, m, s in hsampling.labels.numpy().T
        ]
        for i in range(flat_theta.shape[0])
    ]
    dtype = tf.complex64 if flat_theta.dtype != tf.float64 else tf.complex128
    return tf.reshape(
        tf.constant(result, dtype=dtype),
        list(theta.shape) + [hsampling.labels.shape[1]],
    )


def _spin_spherical_harmonics(
    theta: float, phi: float, l: int, m: int, s: int, precision: Optional[int] = None
) -> float:
    """Spin-weighted spherical_harmonics.

    Examples:

        Comparison against spin-zero spherical harmonics.

        >>> from pytest import approx
        >>> from tensossht.specialfunctions.naive import (
        ...     _spin_spherical_harmonics, spherical_harmonics
        ... )
        >>> for i in range(10):
        ...     l = np.random.randint(5)
        ...     m = np.random.randint(-l, l + 1)
        ...     theta, phi = np.pi * np.random.random(2)
        ...     expected = spherical_harmonics(theta, phi, l, m)
        ...     actual = _spin_spherical_harmonics(theta, phi, l, m, 0)
        ...     assert actual == approx(expected)

        Wikipedia's spin=1 harmonics

        >>> for i in range(10):
        ...     theta, phi = np.pi * np.random.random(2)
        ...     expected = np.sqrt(3 / (8 * np.pi)) * np.sin(theta)
        ...     actual = _spin_spherical_harmonics(theta, phi, 1, 0, 1)
        ...     assert actual == approx(expected)

        >>> for i in range(10):
        ...     theta, phi = np.pi * np.random.random(2)
        ...     factor = -np.sqrt(3 / (16 * np.pi))
        ...     expected = factor * (1 - np.cos(theta)) * np.exp(1j * phi)
        ...     actual = _spin_spherical_harmonics(theta, phi, 1, 1, 1)
        ...     assert actual == approx(expected)

        >>> for i in range(10):
        ...     theta, phi = np.pi * np.random.random(2)
        ...     factor = -np.sqrt(3 / (16 * np.pi))
        ...     expected = factor * (1 + np.cos(theta)) * np.exp(-1j * phi)
        ...     actual = _spin_spherical_harmonics(theta, phi, 1, -1, 1)
        ...     assert actual == approx(expected)

    """
    from mpmath import binomial, cot, exp, factorial, mp, pi, power, sin, sqrt

    if l < np.abs(m) or l < np.abs(s):
        return 0

    if precision is not None:
        old = mp.dps
        try:
            mp.dps = precision
            return spin_spherical_harmonics(theta, phi, l, m, s)
        finally:
            mp.dps = old

    if theta == 0:
        theta = 1e-32

    return (
        (1 if m % 2 == 0 else -1)
        * sqrt(
            factorial(l + m)
            * factorial(l - m)
            * (2 * l + 1)
            / (4 * pi * factorial(l + s) * factorial(l - s))
        )
        * power(sin(theta / 2), 2 * l)
        * sum(
            (
                binomial(l - s, r)
                * binomial(l + s, r + s - m)
                * (1 if (l - r - s) % 2 == 0 else -1)
                * exp(1j * m * phi)
                * power(cot(theta / 2), 2 * r + s - m)
                for r in range(l - s + 1)
            )
        )
    )
