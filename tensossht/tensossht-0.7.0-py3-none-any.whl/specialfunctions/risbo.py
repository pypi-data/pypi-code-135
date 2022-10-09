"""
Risbo Recurrence
================

API
---

.. autofunction:: tensossht.specialfunctions.risbo.wignerd
.. autofunction:: tensossht.specialfunctions.risbo.recurrence
.. autofunction:: tensossht.specialfunctions.risbo.sparse_recurrence
.. autofunction:: tensossht.specialfunctions.risbo.straightforward

.. autofunction:: tensossht.specialfunctions.risbo.initial
"""
from typing import List, Optional, Tuple, Type, Union

import numpy as np
import tensorflow as tf


def sqrt_ints(lmax: int = 10000) -> List:
    from math import sqrt

    return [sqrt(i) for i in range(2 * lmax + 1)]


def initial(l: int, beta: Union[float, np.ndarray, tf.Tensor]) -> tf.Tensor:
    """D-matrices for L=0 and L=1.

    Example:

        >>> from pytest import approx
        >>> from tensossht.specialfunctions import naive
        >>> from tensossht.specialfunctions.risbo import initial
        >>> np.array(initial(0, np.pi / 2)) == approx(naive.wignerd(0, 0, 0, np.pi / 2))
        True
        >>> np.array(initial(0, np.pi / 3)) == approx(naive.wignerd(0, 0, 0, np.pi / 3))
        True
        >>> np.array(initial(1, np.pi / 7)) == approx(
        ...     naive.wignerd(1, beta=np.pi / 7).astype(float)
        ... )
        True

    """

    _beta = tf.convert_to_tensor(beta)
    if l == 0 and isinstance(beta, (np.ndarray, tf.Tensor)):
        return tf.ones((*_beta.shape, 1, 1), dtype=_beta.dtype)
    elif l == 0:
        return tf.ones((1, 1), dtype=_beta.dtype)
    else:
        return (
            (
                (tf.cos(_beta / 2) * tf.cos(_beta / 2))[..., tf.newaxis, tf.newaxis]
                * tf.constant([[1, 0, 0], [0, 0, 0], [0, 0, 1]], dtype=_beta.dtype)
            )
            + (
                (tf.sin(_beta) / tf.sqrt(tf.cast(2, _beta.dtype)))[
                    ..., tf.newaxis, tf.newaxis
                ]
                * tf.constant([[0, 1, 0], [-1, 0, 1], [0, -1, 0]], dtype=_beta.dtype)
            )
            + (
                (tf.sin(_beta / 2) * tf.sin(_beta / 2))[..., tf.newaxis, tf.newaxis]
                * tf.constant([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=_beta.dtype)
            )
            + (
                tf.cos(_beta)[..., tf.newaxis, tf.newaxis]
                * tf.constant([[0, 0, 0], [0, 1, 0], [-0, 0, 0]], dtype=_beta.dtype)
            )
        )


def sparse_recurrence(
    l: int,
    beta: float,
    sqrts: Optional[List[float]] = None,
    dtype: Union[str, Type] = tf.float32,
) -> Tuple[tf.SparseTensor, tf.SparseTensor]:
    """Risbo recurrense using sparse tensors."""
    from functools import partial
    from itertools import product
    from math import cos, sin

    if sqrts is None:
        sqrts = sqrt_ints()

    def matrix_indices(i4, shape):
        return i4[0] * shape[1] + i4[1], i4[2] * shape[3] + i4[3]

    coshb = -cos(beta / 2) / (2 * l - 1)
    sinhb = sin(beta / 2) / (2 * l - 1)
    shape = (2 * l + 1, 2 * l + 1, 2 * l - 1, 2 * l - 1)

    def indices():
        for k in range(1, 2 * l):
            yield 1, k, k - 1, 0
            yield 1, k + 1, k - 1, 0
        for i, k in product(range(2, 2 * l), range(1, 2 * l)):
            yield i, k, k - 1, i - 2
            yield i, k, k - 1, i - 1
            yield i, k + 1, k - 1, i - 2
            yield i, k + 1, k - 1, i - 1
        for k in range(1, 2 * l):
            yield 2 * l, k, k - 1, 2 * l - 2
            yield 2 * l, k + 1, k - 1, 2 * l - 2

    def values():
        assert sqrts is not None
        for k in range(1, 2 * l):
            yield sqrts[2 * l - 1] * sqrts[(2 * l - k)] * coshb
            yield sqrts[2 * l - 1] * sqrts[k] * sinhb
        for i, k in product(range(2, 2 * l), range(1, 2 * l)):
            yield -sqrts[i - 1] * sqrts[2 * l - k] * sinhb
            yield sqrts[2 * l - i] * sqrts[2 * l - k] * coshb
            yield sqrts[i - 1] * sqrts[k] * coshb
            yield sqrts[2 * l - i] * sqrts[k] * sinhb
        for k in range(1, 2 * l):
            yield -sqrts[2 * l - 1] * sqrts[2 * l - k] * sinhb
            yield sqrts[2 * l - 1] * sqrts[k] * coshb

    A = tf.SparseTensor(
        indices=list(map(partial(matrix_indices, shape=shape), indices())),
        values=tf.constant(list(values()), dtype=dtype),
        dense_shape=((2 * l + 1) ** 2, (2 * l - 1) ** 2),
    )

    coshb = -cos(beta / 2) / (2 * l)
    sinhb = sin(beta / 2) / (2 * l)
    shape = (2 * l + 1, 2 * l + 1, 2 * l + 1, 2 * l + 1)

    def indices_b():
        for i in range(0, 2 * l):
            yield 0, i, i + 1, 1
            yield 0, i + 1, i + 1, 1
        for k, i in product(range(1, 2 * l), range(0, 2 * l)):
            yield k, i, i + 1, k
            yield k, i, i + 1, k + 1
            yield k, i + 1, i + 1, k
            yield k, i + 1, i + 1, k + 1
        for i in range(0, 2 * l):
            yield 2 * l, i, i + 1, 2 * l
            yield 2 * l, i + 1, i + 1, 2 * l

    def values_b():
        assert sqrts is not None
        for i in range(0, 2 * l):
            yield sqrts[2 * l - i] * sqrts[2 * l] * coshb
            yield -sqrts[i + 1] * sqrts[2 * l] * sinhb
        for k, i in product(range(1, 2 * l), range(0, 2 * l)):
            yield sqrts[2 * l - i] * sqrts[k] * sinhb
            yield sqrts[2 * l - i] * sqrts[2 * l - k] * coshb
            yield sqrts[i + 1] * sqrts[k] * coshb
            yield -sqrts[i + 1] * sqrts[2 * l - k] * sinhb
        for i in range(0, 2 * l):
            yield sqrts[2 * l - i] * sqrts[2 * l] * sinhb
            yield sqrts[i + 1] * sqrts[2 * l] * coshb

    B = tf.SparseTensor(
        indices=list(map(partial(matrix_indices, shape=shape), indices_b())),
        values=tf.constant(list(values_b()), dtype=dtype),
        dense_shape=((2 * l + 1) ** 2, (2 * l + 1) ** 2),
    )

    return B, A


def wignerd(
    l: int, beta: Union[float, tf.Tensor], sqrts: Optional[List[float]] = None
) -> tf.Tensor:
    """Wigner-d matrix for order l."""

    if sqrts is None:
        sqrts = sqrt_ints()

    _beta = tf.convert_to_tensor(beta)
    current = tf.reshape(initial(1, _beta), shape=(9, 1))
    for ll in range(2, l + 1):
        A, B = sparse_recurrence(ll, _beta, sqrts=sqrts, dtype=_beta.dtype)
        current = tf.sparse.sparse_dense_matmul(
            A, tf.sparse.sparse_dense_matmul(B, current)
        )
    return tf.reshape(current, shape=(2 * l + 1, 2 * l + 1))


def recurrence(l: int, beta: float, dtype: Union[str, Type] = tf.float32) -> tf.Tensor:
    """Simple Risbo recurrence to compute wigner-d matrices.

    This recurrence does not make use of any symmetries.

    Example:

        >>> from pytest import approx
        >>> from tensossht.specialfunctions import naive
        >>> from tensossht.specialfunctions.risbo import recurrence
        >>> R1 = recurrence(l=1, beta=np.pi / 7, dtype=float)
        >>> R2 = recurrence(l=2, beta=np.pi / 7, dtype=float)
        >>> R2R1 = tf.tensordot(R2, R1, axes=[[2, 3], [0, 1]])
        >>> np.array(R2R1)  == approx(naive.wignerd(2, beta=np.pi / 7).astype(float))
        True
        >>> R3 = recurrence(l=3, beta=np.pi / 7, dtype=float)
        >>> R3R2R1 = tf.tensordot(R3, R2R1, axes=[[2, 3], [0, 1]])
        >>> np.array(R3R2R1)  == approx(naive.wignerd(3, beta=np.pi / 7).astype(float))
        True

    """
    if l <= 1:
        return initial(l, beta)

    coshb = -np.cos(beta / 2)
    sinhb = np.sin(beta / 2)
    A = np.zeros(
        (2 * l + 1, 2 * l + 1, 2 * l - 1, 2 * l - 1),
        dtype=getattr(dtype, "as_numpy_dtype", dtype),
    )
    for i in range(1, 2 * l):
        for k in range(1, 2 * l):
            A[i, k, k - 1, i - 1] = (
                np.sqrt((2 * l - i) * (2 * l - k)) * coshb / (2 * l - 1)
            )
            A[i + 1, k, k - 1, i - 1] = -np.sqrt(i * (2 * l - k)) * sinhb / (2 * l - 1)
            A[i, k + 1, k - 1, i - 1] = np.sqrt((2 * l - i) * k) * sinhb / (2 * l - 1)
            A[i + 1, k + 1, k - 1, i - 1] = np.sqrt(i * k) * coshb / (2 * l - 1)

    B = np.zeros(
        (2 * l + 1, 2 * l + 1, 2 * l + 1, 2 * l + 1),
        dtype=getattr(dtype, "as_numpy_dtype", dtype),
    )
    for i in range(0, 2 * l):
        for k in range(0, 2 * l):
            B[k, i, i + 1, k + 1] = np.sqrt((2 * l - i) * (2 * l - k)) / (2 * l) * coshb
            B[k + 1, i, i + 1, k + 1] = np.sqrt((2 * l - i) * (k + 1)) / (2 * l) * sinhb
            B[k, i + 1, i + 1, k + 1] = (
                -np.sqrt((i + 1) * (2 * l - k)) / (2 * l) * sinhb
            )
            B[k + 1, i + 1, i + 1, k + 1] = np.sqrt((i + 1) * (k + 1)) / (2 * l) * coshb
    return tf.tensordot(
        tf.constant(B, dtype=dtype), tf.constant(A, dtype=dtype), axes=[[2, 3], [0, 1]]
    )


def straightforward(
    l: int, m1: int, m2: int, beta: float, sqrts: Optional[List[float]] = None
) -> float:

    if m1 < -l or m1 > l or m2 < -l or m2 > l:
        return 0
    if l <= 1:
        return initial(l, beta).numpy()[m1 + l, m2 + l]

    if sqrts is None:
        sqrts = sqrt_ints()
    if sqrts[-1] != 0:
        sqrts = sqrts + [0.0]

    coshb = -np.cos(beta / 2)
    sinhb = np.sin(beta / 2)

    def previous(i, k):
        return straightforward(l - 1, i, k, beta, sqrts=sqrts)

    def intermediate(i: int, k: int):
        assert isinstance(sqrts, List)
        return (
            sqrts[l - i] * sqrts[l - k] * coshb * previous(i, k)
            + sqrts[l - 1 + i] * sqrts[l - k] * sinhb * previous(i - 1, k)
            - sqrts[l - i] * sqrts[l - 1 + k] * sinhb * previous(i, k - 1)
            + sqrts[l - 1 + i] * sqrts[l - 1 + k] * coshb * previous(i - 1, k - 1)
        ) / (2 * l - 1)

    return (
        sqrts[l - m1] * sqrts[l - m2] * coshb * intermediate(m1 + 1, m2 + 1)
        + sqrts[l + m1] * sqrts[l - m2] * sinhb * intermediate(m1, m2 + 1)
        - sqrts[l - m1] * sqrts[l + m2] * sinhb * intermediate(m1 + 1, m2)
        + sqrts[l + m1] * sqrts[l + m2] * coshb * intermediate(m1, m2)
    ) / (2 * l)


def degree(
    l: int,
    beta: Union[float, List[float], tf.Tensor, np.ndarray],
    previous: Optional[tf.Tensor] = None,
) -> List[tf.Tensor]:

    _beta = tf.convert_to_tensor(value=beta, name="degree")

    if previous is None:
        previous = initial(0 if l == 0 else 1, _beta)
    assert previous is not None

    l = tf.convert_to_tensor(value=l, name="degree")
    l0 = (previous.shape[-1] - 1) // 2
    assert 2 * l0 + 1 == previous.shape[-1]
    result = [previous]
    cosb = tf.cos(_beta / 2, "cos beta")[..., tf.newaxis, tf.newaxis]
    sinb = tf.sin(_beta / 2, "sin beta")[..., tf.newaxis, tf.newaxis]
    sqrts = tf.sqrt(tf.cast(tf.range(2 * l + 1), dtype=_beta.dtype), "sqrts")
    for i in tf.range(l0 + 1, l + 1):
        result.append(_degree_impl(i, cosb, sinb, sqrts[0 : 2 * i + 1], result[-1]))

    return result


@tf.function
def _degree_impl(
    l: tf.Tensor,
    cosb: tf.Tensor,
    sinb: tf.Tensor,
    sqrts: tf.Tensor,
    previous: tf.Tensor,
) -> tf.Tensor:

    zshape: List[Tuple[int, int]] = [(0, 0) for _ in range(len(cosb.shape) - 2)]
    scaled = previous / tf.cast((2 * l) * (2 * l - 1), dtype=previous.dtype)
    intermediate = (
        tf.pad(
            sqrts[-2:0:-1] * sqrts[1:-1, tf.newaxis] * sinb * scaled,
            zshape + [(1, 0), (0, 1)],
        )
        - tf.pad(
            sqrts[1:-1] * sqrts[-2:0:-1, tf.newaxis] * sinb * scaled,
            zshape + [(0, 1), (1, 0)],
        )
        - tf.pad(
            sqrts[-2:0:-1] * sqrts[-2:0:-1, tf.newaxis] * cosb * scaled,
            zshape + [(0, 1), (0, 1)],
        )
        - tf.pad(
            sqrts[1:-1] * sqrts[1:-1, tf.newaxis] * cosb * scaled,
            zshape + [(1, 0), (1, 0)],
        )
    )
    return (
        tf.pad(
            sqrts[:0:-1] * sqrts[1:, tf.newaxis] * sinb * intermediate,
            zshape + [(1, 0), (0, 1)],
        )
        - tf.pad(
            sqrts[1:] * sqrts[:0:-1, tf.newaxis] * sinb * intermediate,
            zshape + [(0, 1), (1, 0)],
        )
        - tf.pad(
            sqrts[:0:-1] * sqrts[:0:-1, tf.newaxis] * cosb * intermediate,
            zshape + [(0, 1), (0, 1)],
        )
        - tf.pad(
            sqrts[1:] * sqrts[1:, tf.newaxis] * cosb * intermediate,
            zshape + [(1, 0), (1, 0)],
        )
    )
