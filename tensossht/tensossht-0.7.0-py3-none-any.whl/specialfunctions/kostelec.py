"""
Kostelec Recurrence
===================

Implementation of the recurrence from [Kostelec, Rockmore (2008)].

API
---

.. autofunction:: tensossht.specialfunctions.kostelec.legendre
.. autofunction:: tensossht.specialfunctions.kostelec.wignerd
.. autofunction:: tensossht.specialfunctions.kostelec.logfact
"""
from textwrap import dedent
from typing import Optional, Tuple, Union

import numpy as np
import tensorflow as tf

from tensossht.references import REFERENCES


@tf.function
def logfact(
    n: Union[int, tf.Tensor], dtype: Union[str, tf.DType] = tf.float32
) -> tf.Tensor:
    """Log of factorial 0 <= i <= n.

    Example:

        >>> from tensossht.specialfunctions.kostelec import logfact
        >>> tf.exp(logfact(5)).numpy().astype(float).round(2)
        array([  1.,   1.,   2.,   6.,  24., 120.])

    """

    initial = tf.range(1, n + 1, dtype=tf.dtypes.as_dtype(dtype).real_dtype)
    logfacts = tf.scan(lambda a, x: a + x, tf.math.log(initial))
    return tf.concat([tf.zeros(1, dtype=logfacts.dtype), logfacts], 0)


def legendre(
    beta: Union[float, tf.Tensor],
    lmax: Optional[int] = None,
    lmin: int = 0,
    mmin: int = 0,
    mmax: Optional[int] = None,
    labels: Optional[Union[np.ndarray, tf.Tensor]] = None,
    scaled: bool = True,
) -> tf.Tensor:
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

    assert lmax is not None
    _beta: tf.Tensor = tf.convert_to_tensor(beta, name="beta")
    logfacts = logfact(2 * lmax + 2, dtype=_beta.dtype)

    if scaled:
        return _scaled_legendre_impl(_beta, labels, logfacts)
    else:
        return _legendre_impl(_beta, labels, logfacts)


legendre.__doc__ = (
    dedent(
        r"""Legendre polynomials via the Kostelec recurrence.

    See [Kostelec, Rockmore (2008)], equations 4.6, 4.10, and 4.11. Specifically, They
    are implemented here with :math:`m'=0`, reproduced and simplified below:

    .. math::

        d^j_{j0}(\beta) = \sqrt{\frac{(2j)!}{j!^2}} 2^{-j}\sin^j\beta

        \tilde{d}^j_{m0} = \sqrt{\frac{2}{3j + 1}} d^j_{m0}

        \tilde{d}^{j+1}_{m0} =
            \sqrt{\frac{(2j + 3)(2j+1)}{(j + 1)^2 - m^2}}\cos\beta \tilde{d}^j_{m0}
            - \sqrt{\frac{(2j + 3)(j^2 - m^2)}{(2j - 1)(j + 1)^2 - m^2}}
                \tilde{d}^{j-1}_{m0}

    %s

    Args:
        beta: Scalar or multi-dimenionsonal vector of values. ``beta`` corresponds to
            ``x=tf.cos(beta)`` in other formulations of the legendre polynomial.
        lmax: If given, all values ``lmax >= l >= lmin`` and ``mmax >= m >= mmin`` will
            be computed. Otherwise, ``labels`` should be given as input.
        lmin: Minimum ``l`` value.
        mmax: Maximum ``m``, defaults to ``lmax``.
        mmin: Minimum ``m`` value.
        labels: a 2 by n vector of ``(l, m)`` values. If given, then ``lmax`` should
            not.
        scaled: If ``True``, then does not take into account the scaling
            :math:`\sqrt{\frac{(l - m)!}{(l + m)!}}`. The scaling makes the function
            numerically well-behaved.

    Example:

        There are two means of calling this function. Either the labels are given
        explicitly as as 2 by n vector, or they are specified via ``lmax``, ``lmin``,
        ``mmax``, and ``mmin``. In the latter case, the labels are obtained via
        :py:func:`~tensossht.specialfunctions.legendre_labels`. The input ``beta`` can
        be a ``float`` or anything convertible to a tensorflow tensor:

        >>> from pytest import approx
        >>> from tensossht import legendre_labels
        >>> from tensossht.specialfunctions.kostelec import legendre
        >>> lmax = 4
        >>> legpol = legendre(beta=0.4, lmax=lmax)
        >>> legpol.numpy().round(4)
        array([ 1.    ,  0.9211, -0.2754,  0.7725, -0.4393,  0.0929,  0.5719,
               -0.5466,  0.1913, -0.033 ], dtype=float32)

        We can verify the two methods are equivalent:

        >>> labels = legendre_labels(lmax=lmax)
        >>> labels
        <tf.Tensor: shape=(2, 10), dtype=int32, numpy=
        array([[0, 1, 1, 2, 2, 2, 3, 3, 3, 3],
               [0, 0, 1, 0, 1, 2, 0, 1, 2, 3]], dtype=int32)>
        >>> assert legpol.numpy() == approx(legendre(beta=0.4, labels=labels).numpy())

        We can check that the legendre polynomials are correct against a naive,
        brute-force implementation:

        >>> from tensossht.specialfunctions import naive
        >>> beta = tf.random.uniform([3], dtype=tf.float64) * np.pi
        >>> legpol = legendre(beta, labels=labels, scaled=False)
        >>> for actual, (l, m) in zip(legpol.numpy().T, labels.numpy().T):
        ...    expected = [float(naive.legendre(l, m, np.cos(b))) for b in beta]
        ...    assert actual == approx(expected)

        Note that the input to the different legendre functions in the code are not all
        equivalent. They will differ by whether they take ``beta`` or ``tf.cos(beta)``
        as input, and potentially by a keyword-triggered scaling.
    """
    )
    % REFERENCES["KR"]
)


@tf.function
def _legendre_impl(
    beta: tf.Tensor, labels: tf.Tensor, logfacts: tf.Tensor
) -> tf.Tensor:
    return tf.exp(
        0.5
        * (
            tf.math.lgamma(tf.cast(labels[0] + labels[1] + 1, dtype=beta.dtype))
            - tf.math.lgamma(tf.cast(labels[0] - labels[1] + 1, dtype=beta.dtype))
        )
    ) * _scaled_legendre_impl(beta, labels, logfacts)


@tf.function
def _scaled_legendre_impl(
    beta: tf.Tensor, labels: tf.Tensor, logfacts: tf.Tensor
) -> tf.Tensor:
    r"""Implementation of the Kostelec recurrence limited to m'=0."""
    dtype = beta.dtype
    valid = labels[0] >= tf.abs(labels[1])
    l = labels[0]
    m = tf.where(valid, tf.abs(labels[1]), 0)

    sinb = tf.sin(beta)
    cosb = tf.cos(beta)

    # kostelec 4.10 + 4.6
    sinterm = tf.cast((m // 2), dtype=dtype) * (
        tf.math.log(tf.expand_dims(sinb * sinb, -1))
        - tf.math.log(tf.cast(4, dtype=dtype))
    )
    midterm = tf.exp(
        0.5
        * (
            tf.gather(logfacts, 2 * m + 1, axis=0)
            - tf.math.log(tf.constant(2, dtype=dtype))
        )
        - tf.gather(logfacts, m, axis=0)
        + tf.where(tf.math.is_nan(sinterm), tf.zeros_like(sinterm), sinterm)
    ) * tf.where(
        m % 2 == 1,
        -0.5 * tf.expand_dims(sinb, -1),
        tf.expand_dims(tf.ones_like(beta), -1),
    )

    # kostelec 4.10 + 4.11, assuming d^{j-1}{m0} is zero...
    highterm = tf.where(
        l == m,
        midterm,
        tf.sqrt(tf.cast(2 * m + 3, dtype=dtype)) * tf.expand_dims(cosb, -1) * midterm,
    )

    j = m + 2
    for _ in tf.range(tf.reduce_max(l - j) + 1):
        lowterm, midterm = midterm, highterm
        coeffm = (
            tf.sqrt(tf.cast(4 * j * j - 1, dtype=dtype))
            / tf.sqrt(tf.cast(j * j - m * m, dtype))
            * tf.expand_dims(cosb, -1)
        )
        coeffl = tf.sqrt(
            tf.cast((2 * j + 1) * ((j - 1) * (j - 1) - m * m), dtype=dtype)
        ) / tf.sqrt(tf.cast((2 * j - 3) * (j * j - m * m), dtype))
        highterm = tf.where(j > l, highterm, coeffm * midterm - coeffl * lowterm)
        j = tf.where(j <= l, j + 1, j)

    result = highterm * tf.sqrt(
        tf.cast(2, dtype=dtype) / tf.cast(2 * l + 1, dtype=dtype)
    )
    return tf.where(
        valid,
        tf.where(tf.logical_or(labels[1] >= 0, labels[1] % 2 == 0), result, -result),
        0,
    )


def wignerd(
    beta: Union[float, tf.Tensor],
    *,
    labels: Optional[tf.Tensor] = None,
    lmax: Optional[int] = None,
    lmin: int = 0,
    mmin: Optional[int] = None,
    mmax: Optional[int] = None,
    mpmin: Optional[int] = None,
    mpmax: Optional[int] = None,
    scaled: bool = True,
) -> tf.Tensor:
    f"""Wigner-d via the Kostelec recurrence.

    See [Kostelec, Rockmore (2008)], equations 4.6, 4.10, and 4.11.

    {REFERENCES['KR']}
    """
    from tensossht.sampling import wignerd_labels

    if not scaled:
        raise NotImplementedError

    if labels is None and lmax is None:
        raise ValueError("Missing on of labels or (lmax, lmin...)")
    if labels is None:
        assert isinstance(lmax, int)
        labels = wignerd_labels(
            lmax=lmax, lmin=lmin, mmin=mmin, mmax=mmax, mpmin=mpmin, mpmax=mpmax
        )
    else:
        lmax = tf.reduce_max(labels[0])
    assert labels is not None
    _beta = tf.convert_to_tensor(beta, name="beta")
    logfacts = logfact(2 * lmax + 2, dtype=_beta.dtype)  # type: ignore
    epsilon = tf.constant({tf.float16: 1e-7}.get(_beta.dtype, 1e-45), dtype=_beta.dtype)
    condition = tf.logical_and(
        labels[0] >= tf.abs(labels[1]), labels[0] >= tf.abs(labels[2])
    )
    labels = tf.where(condition, labels, 0)
    result = _wignerd_impl(_beta, labels, logfacts, epsilon)
    return tf.where(condition, result, 0)


@tf.function
def _wignerd_impl(
    beta: tf.Tensor,
    labels: tf.Tensor,
    logfacts: tf.Tensor,
    epsilon: Union[float, tf.Tensor] = 1e-45,
) -> tf.Tensor:
    r"""Implementation of the Kostelec recurrence."""
    dtype = beta.dtype

    symlabs, signs = _symmetries(labels)

    l = symlabs[0]
    m = symlabs[1]
    mp = symlabs[2]
    sinb = tf.sin(beta / 2)
    cosb = tf.cos(beta / 2)

    factors = tf.sqrt(2 / tf.cast(2 * l + 1, dtype=dtype))
    factors = tf.where(signs >= 0, factors, -factors)

    def logzero(exponent, logterm):
        """Deals with zeros in the log-space terms."""
        return tf.cast(exponent, dtype=beta.dtype) * tf.math.log(
            tf.where(logterm <= epsilon, epsilon, logterm)
        )

    # kostelec 4.10 + 4.6
    midterm = (
        tf.exp(
            0.5
            * (
                tf.gather(logfacts, 2 * m + 1, axis=0)
                - tf.gather(logfacts, m + mp, axis=0)
                - tf.gather(logfacts, m - mp, axis=0)
                - tf.math.log(tf.constant(2, dtype=dtype))
            )
            + logzero((m + mp) // 2, tf.expand_dims(cosb * cosb, -1))
            + logzero((m - mp) // 2, tf.expand_dims(sinb * sinb, -1))
        )
        * tf.where(
            (m + mp) % 2 == 1,
            tf.expand_dims(cosb, -1),
            tf.expand_dims(tf.ones_like(beta), -1),
        )
        * tf.where(
            (m - mp) % 2 == 1,
            tf.expand_dims(-sinb, -1),
            tf.expand_dims(tf.ones_like(beta), -1),
        )
    )

    # kostelec 4.10 + 4.11, assuming d^{j-1}{m0} is zero...
    highterm = tf.where(
        l == m,
        midterm,
        tf.sqrt(
            tf.cast(2 * m + 3, dtype=dtype)
            / tf.cast((m + 1) * (m + 1) - mp * mp, dtype=dtype)
        )
        * (
            tf.cast(m + 1, dtype=dtype) * tf.expand_dims(tf.cos(beta), -1)
            - tf.cast(mp, dtype=dtype)
        )
        * midterm,
    )

    j = m + 2
    for _ in tf.range(tf.reduce_max(l - j) + 1):
        lowterm, midterm = midterm, highterm
        coeffm = tf.sqrt(
            tf.cast((2 * j + 1) * (2 * j - 1), dtype=dtype)
            / tf.cast((j * j - m * m) * (j * j - mp * mp), dtype=dtype)
        ) * (
            tf.expand_dims(tf.cos(beta), -1) * tf.cast(j, dtype=dtype)
            - tf.cast(m * mp, dtype=dtype) / tf.cast(j - 1, dtype=dtype)
        )
        coeffl = (
            tf.sqrt(
                tf.cast(
                    (2 * j + 1)
                    * ((j - 1) * (j - 1) - m * m)
                    * ((j - 1) * (j - 1) - mp * mp),
                    dtype=dtype,
                )
                / tf.cast(
                    (2 * j - 3) * (j * j - m * m) * (j * j - mp * mp), dtype=dtype
                )
            )
            * tf.cast(j, dtype=dtype)
            / tf.cast(j - 1, dtype=dtype)
        )
        highterm = tf.where(j > l, highterm, coeffm * midterm - coeffl * lowterm)
        j = tf.where(j <= l, j + 1, j)

    return highterm * factors


def _symmetries(labels: tf.Tensor) -> Tuple[tf.Tensor, tf.Tensor]:
    """Computes factor while making sure m >= mp >= 0."""
    l = labels[0]
    ms = labels[1:]

    size_condition = tf.abs(ms[0]) < tf.abs(ms[1])
    ms = tf.where(size_condition, ms[::-1, :], ms)

    sign_condition = ms[0] < 0
    ms = tf.where(sign_condition, -ms, ms)

    factors = tf.where(
        tf.logical_and(size_condition, (ms[0] - ms[1]) % 2 == 1)
        != tf.logical_and(sign_condition, (ms[0] - ms[1]) % 2 == 1),
        -1,
        1,
    )
    return (
        tf.concat(
            [tf.expand_dims(l, 0), tf.expand_dims(ms[0], 0), tf.expand_dims(ms[1], 0)],
            axis=0,
        ),
        factors,
    )
