from typing import List, Optional, Union

import numpy as np
import tensorflow as tf


def straightforward(l: int, m: int, x: float, scaled: bool = False) -> float:
    """Numerical recipes implementation of Legendre polynomial.

    Computes the associated legendre functions using the recursive method from numerical
    recipes.

    Example:

        >>> from tensossht.specialfunctions import numericalrecipes as nr
        >>> from tensossht.specialfunctions import naive
        >>> from random import random
        >>> from pytest import approx
        >>> for l in range(5):
        ...     for m in range(0, l + 1):
        ...         x = random()
        ...         expected = naive.legendre(l, m, x)
        ...         assert nr.straightforward(l, m, x) == approx(expected)

    """
    from math import pi, sqrt

    if m > l:
        raise ValueError("Legendre polynomials require m <= l.")
    if m < 0:
        raise ValueError("Legendre polynomials require m >= 0.")

    if scaled:
        final_factor = sqrt(4 * pi / (2 * l + 1))
    else:
        factorial: int = 1
        for i in range(l - m + 1, l + m + 1):
            factorial *= i
        final_factor = sqrt(4 * pi * factorial / (2 * l + 1))

    pmm: float = 1.0
    omx2: float = (1 - x) * (1 + x)
    fact: float = 1.0
    for i in range(1, m + 1):
        pmm *= omx2 * fact / (fact + 1)
        fact += 2
    pmm = sqrt((2 * m + 1) * pmm / (4 * pi))
    if m % 2 == 1:
        pmm = -pmm
    if l == m:
        return pmm * final_factor
    pmmp1 = x * sqrt(2 * m + 3) * pmm
    if l == m + 1:
        return pmmp1 * final_factor
    oldfact = sqrt(2 * m + 3)
    pll = 1
    for ll in range(m + 2, l + 1):
        fact = sqrt((4 * ll * ll - 1) / (ll * ll - m * m))
        pll = (x * pmmp1 - pmm / oldfact) * fact
        oldfact = fact
        pmm = pmmp1
        pmmp1 = pll
    return pll * final_factor


def legendre(
    x: Union[float, List[float], tf.Tensor],
    lmax: Optional[int] = None,
    lmin: int = 0,
    mmax: Optional[int] = None,
    mmin: Optional[int] = 0,
    labels: Optional[Union[np.ndarray, tf.Tensor]] = None,
    scaled: bool = True,
) -> tf.Tensor:
    r"""Numerical recipes implementation of Legendre polynomial.

    Computes the associated legendre functions using the recursive method from numerical
    recipes, with a tensorflow implementation.

    Args:
        x: Scalar or multi-dimenionsonal vector of values. ``x`` corresponds to
            ``x=tf.cos(beta)`` in other formulations of the legendre polynomial.
        lmax: If given, all values ``lmax >= l >= lmin`` and ``mmax >= m >= mmin`` will
            be computed. Otherwise, ``labels`` should be given as input.
        lmin: Minimum ``l`` value.
        mmax: Maximum ``m``, defaults to ``lmax``.
        mmin: Minimum ``m`` value.
        labels: a 2 by n vector of ``(l, m)`` values. If given, then ``lmax`` should
            not.
        scaled: If ``True``, then does not take into account the scaling
            :math:`\\sqrt(\\frac{(l - m)!}{(l + m)!})`. The scaling makes the function
            numerically well-behaved.

    Example:

        There are two means of calling this function. Either the labels are given
        explicitly as as 2 by n vector, or they are specified via ``lmax``, ``lmin``,
        ``mmax``, and ``mmin``. In the latter case, the labels are obtained via
        :py:func:`~tensossht.specialfunctions.legendre_labels`. The input ``beta`` can
        be a ``float`` or anything convertible to a tensorflow tensor:

        >>> from pytest import approx
        >>> from tensossht import legendre_labels
        >>> from tensossht.specialfunctions.numericalrecipes import legendre
        >>> lmax = 4
        >>> legpol = legendre(x=tf.cos(0.4), lmax=lmax)
        >>> legpol.numpy().round(4)
        array([ 1.    ,  0.9211, -0.2754,  0.7725, -0.4393,  0.0929,  0.5719,
               -0.5466,  0.1913, -0.033 ], dtype=float32)

        We can verify the two methods are equivalent:

        >>> labels = legendre_labels(lmax=lmax)
        >>> labels
        <tf.Tensor: shape=(2, 10), dtype=int32, numpy=
        array([[0, 1, 1, 2, 2, 2, 3, 3, 3, 3],
               [0, 0, 1, 0, 1, 2, 0, 1, 2, 3]], dtype=int32)>
        >>> with_labels = legendre(x=tf.cos(0.4), labels=labels)
        >>> assert legpol.numpy() == approx(with_labels.numpy())

        We can check that the legendre polynomials are correct against a naive,
        brute-force implementation:

        >>> from tensossht.specialfunctions import naive
        >>> beta = tf.random.uniform([3], dtype=tf.float64) * np.pi
        >>> legpol = legendre(tf.cos(beta), labels=labels, scaled=False)
        >>> for actual, (l, m) in zip(legpol.numpy().T, labels.numpy().T):
        ...    expected = [float(naive.legendre(l, m, np.cos(b))) for b in beta]
        ...    assert actual == approx(expected)

        Note that the input to the different legendre functions in the code are not all
        equivalent. They will differ by whether they take ``beta`` or ``tf.cos(beta)``
        as input, and potentially by a keyword-triggered scaling.
        All values (l, m) as obtained from :py:func:`legendre_labels` are computed.
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
        lmax = tf.reduce_max(labels)
    assert labels is not None

    _x = tf.convert_to_tensor(x, name="x")
    xshape, lshape = _x.shape, labels[..., 0, :].shape
    _x = tf.reshape(_x, shape=(*xshape, *(1 for _ in lshape)), name="x")
    labels = tf.reshape(labels, shape=(*(1 for _ in xshape), *labels.shape), name="l_m")

    return _legendre_impl(_x, labels, scaled=scaled)


@tf.function
def _legendre_impl(x: tf.Tensor, labels: tf.Tensor, scaled: bool = False) -> tf.Tensor:
    """Tensorflow graph function implementation of the legendre functions."""

    l, m = labels[..., 0, :], labels[..., 1, :]
    pmm = tf.ones([a if a != 1 else b for a, b in zip(x.shape, m.shape)], dtype=x.dtype)
    omx2 = (1 - x) * (1 + x)
    for i in tf.range(1, tf.reduce_max(m) + 1):
        pmm = tf.where(
            i <= m,
            pmm
            * omx2
            * tf.cast(2 * i - 1, dtype=x.dtype)
            / tf.cast(2 * i, dtype=x.dtype),
            pmm,
        )
    pmm = tf.sqrt(
        tf.cast(2 * m + 1, dtype=x.dtype) * pmm / tf.constant(4 * np.pi, dtype=x.dtype)
    )
    pmm = tf.where(m % 2 == 1, -pmm, pmm)

    pmmp1 = tf.where(m < l, x * tf.sqrt(tf.cast(2 * m + 3, dtype=x.dtype)) * pmm, pmm)
    pmm = tf.where(l == m + 1, pmmp1, pmm)
    oldfactor = tf.sqrt(tf.cast(2 * m + 3, dtype=x.dtype))
    factor = oldfactor
    pll = pmm
    i = m + 2
    for _ in tf.range(tf.reduce_max(l - m + 2) + 1):
        factor = tf.sqrt(
            tf.cast(4 * i * i - 1, dtype=x.dtype)
            / tf.cast(i * i - m * m, dtype=x.dtype)
        )
        pll = tf.where(i <= l, (x * pmmp1 - pmm / oldfactor) * factor, pmmp1)
        oldfactor = factor
        pmm = tf.where(i <= l, pmmp1, pmm)
        pmmp1 = tf.where(i <= l, pll, pmmp1)
        i += 1

    result = pll * tf.sqrt(
        tf.constant(4 * np.pi, dtype=x.dtype) / tf.cast(2 * l + 1, dtype=x.dtype)
    )
    if not scaled:
        result *= tf.exp(
            0.5
            * (
                tf.math.lgamma(tf.cast(l + m + 1, dtype=result.dtype))
                - tf.math.lgamma(tf.cast(l - m + 1, dtype=result.dtype))
            )
        )
    return result
