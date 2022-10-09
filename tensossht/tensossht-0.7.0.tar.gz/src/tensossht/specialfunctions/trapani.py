"""
Trapani Recurrence
==================

Implementation of the recurrence from [Trapani, Navaza (2006)].

API
---

.. autofunction:: tensossht.specialfunctions.trapani.straightforward
.. autofunction:: tensossht.specialfunctions.trapani.deltas

.. autofunction:: tensossht.specialfunctions.trapani.full_tensor
.. autofunction:: tensossht.specialfunctions.trapani.symmetrized_index
.. autofunction:: tensossht.specialfunctions.trapani.linear_index
.. autofunction:: tensossht.specialfunctions.trapani.ncoeffs
.. autofunction:: tensossht.specialfunctions.trapani.order_from_ncoeffs

.. autofunction:: tensossht.specialfunctions.trapani.delta_ll0
.. autofunction:: tensossht.specialfunctions.trapani.delta_llm
.. autofunction:: tensossht.specialfunctions.trapani._delta_lmmp_impl
"""
from typing import Optional, Tuple, Type, Union, cast

import numpy as np
import tensorflow as tf

from tensossht.references import REFERENCES
from tensossht.typing import Array, TFArray


def ncoeffs(l: int) -> int:
    """Number of coefficients with 0 <= m_1 <= m_2 <= l."""
    return ((l + 3) * l) // 2 + 1


def order_from_ncoeffs(n: int) -> int:
    """Computes l for a given number of coefficients.

    In practice, this is the inverse of ncoeffs.

    Example:

        >>> from tensossht.specialfunctions.trapani import order_from_ncoeffs, ncoeffs
        >>> order_from_ncoeffs(ncoeffs(1))
        1
        >>> order_from_ncoeffs(ncoeffs(2))
        2
        >>> order_from_ncoeffs(ncoeffs(20))
        20

    """
    return int(np.max(np.roots(np.array([1, 3, -2 * (n - 1)]))))


def linear_index(m1: int, m2: int) -> int:
    """Linear index for a given (m1, m2) triplet."""
    assert m2 >= 0 and m2 <= m1
    return 0 if m1 == m2 == 0 else ncoeffs(m1 - 1) + m2


def symmetrized_index(l: int, m1: int, m2: int, factor: int = 1) -> Tuple[int, int]:
    """Computes index and factor to go from compressed results to full tensor.

    Only 0 <= m2 <= m1 are represented in the recursion. Given l, and any general m1 and
    m2, this funtion outputs the index and factor needed to recover the full symmetrized
    wignerd value.

    Example:

        Evidently, this function does not do much when it tries to access those elements
        that are explictly present in the compressed form:

        >>> from tensossht.specialfunctions.trapani import (
        ...     recursion_tensor as R, symmetrized_index, linear_index
        ... )
        >>> compressed = R(5) @ R(4) @ R(3) @ R(2) @ R(1) @ R(0)
        >>> index, factor = symmetrized_index(5, 4, 3)
        >>> factor == 1
        True
        >>> index == linear_index(4, 3)
        True

        We can check against the wigner-d function that the correct factor was
        recovered.

        >>> from pytest import approx
        >>> from tensossht.specialfunctions import naive
        >>> index, factor = symmetrized_index(5, -4, -3)
        >>> index, factor
        (13, -1)
        >>> float(compressed[index] * factor)== approx(naive.wignerd(5, -4, -3))
        True

    """
    if abs(m1) > l or abs(m2) > l:
        return 0, 0
    if m2 <= m1 and m2 >= 0:
        return linear_index(m1, m2), factor
    if m1 < 0 and m2 < 0:
        return symmetrized_index(l, -m2, -m1, factor)
    if m1 < 0:
        return symmetrized_index(l, -m1, m2, factor if (l - m2) % 2 == 0 else -factor)
    if m2 < 0:
        return symmetrized_index(l, m1, -m2, factor if (l - m1) % 2 == 0 else -factor)
    return symmetrized_index(l, m2, m1, factor if (m2 - m1) % 2 == 0 else -factor)


def outer_recursion_tensor(l: int, dtype: Union[Type, str] = tf.float32) -> TFArray:
    from tensorflow import constant

    from .trapani import linear_index as i

    dtype = tf.constant(1, dtype=dtype).numpy().dtype
    result = np.zeros((ncoeffs(l), ncoeffs(l - 1)), dtype=dtype)
    result[i(l, 0), i(l - 1, 0)] = -np.sqrt(1 - 1 / (2 * l))
    for m in range(1, l + 1):
        result[i(l, m), i(l - 1, m - 1)] = np.sqrt(
            (l * (2 * l - 1)) / ((l + m) * (l + m - 1) * 2)
        )
    return constant(result, dtype)


def outer_recursion_sparse(
    l: int, dtype: Union[Type, str] = tf.float32
) -> tf.SparseTensor:
    from .trapani import linear_index as i

    indices = [(i(l, m), i(l - 1, max(m - 1, 0))) for m in range(l + 1)]
    values = [-np.sqrt(1 - 1 / (2 * l))] + [
        np.sqrt((l * (2 * l - 1)) / ((l + m) * (l + m - 1) * 2))
        for m in range(1, l + 1)
    ]
    return tf.SparseTensor(
        indices=indices,
        values=tf.constant(values, dtype=dtype),
        dense_shape=(ncoeffs(l), ncoeffs(l - 1)),
    )


def inner_recursion_tensor(l: int, dtype: Union[Type, str] = tf.float32) -> TFArray:
    from .trapani import linear_index as i

    dtype = tf.constant(1, dtype=dtype).numpy().dtype
    tensor = np.zeros((ncoeffs(l), ncoeffs(l)), dtype=dtype)
    for m1 in range(l):
        for m2 in range(1, m1 + 1):
            tensor[i(m1, m2), i(m1 + 1, m2)] = (2 * m2) / np.sqrt(
                (l - m1) * (l + m1 + 1)
            )
    for m1 in range(l - 1):
        for m2 in range(m1 + 1):
            tensor[i(m1, m2), i(m1 + 2, m2)] = -np.sqrt(
                (l - m1 - 1) * (l + m1 + 2) / ((l - m1) * (l + m1 + 1))
            )
    II = np.identity(tensor.shape[0])
    result = II
    for l in range(l):
        result = tensor @ result + II
    return tf.constant(result, dtype=dtype)


def inner_recursion_sparse(
    l: int, dtype: Union[Type, str] = tf.float32
) -> tf.SparseTensor:
    from scipy.sparse import csc_matrix, eye

    from .trapani import linear_index as i

    rows = [i(m1, m2) for m1 in range(l) for m2 in range(1, m1 + 1)] + [
        i(m1, m2) for m1 in range(l - 1) for m2 in range(m1 + 1)
    ]
    columns = [i(m1 + 1, m2) for m1 in range(l) for m2 in range(1, m1 + 1)] + [
        i(m1 + 2, m2) for m1 in range(l - 1) for m2 in range(m1 + 1)
    ]
    values = [
        (2 * m2) / np.sqrt((l - m1) * (l + m1 + 1))
        for m1 in range(l)
        for m2 in range(1, m1 + 1)
    ] + [
        -np.sqrt((l - m1 - 1) * (l + m1 + 2) / ((l - m1) * (l + m1 + 1)))
        for m1 in range(l - 1)
        for _ in range(m1 + 1)
    ]
    tensor = csc_matrix((values, (rows, columns)), shape=(ncoeffs(l), ncoeffs(l)))
    current = tensor.copy()
    result = current + eye(ncoeffs(l), format="csc")
    for _ in range(l):
        current *= tensor
        result += current
    return tf.SparseTensor(
        indices=list(zip(*result.nonzero())),
        values=tf.constant(np.array(result[result.nonzero()]).squeeze(), dtype=dtype),
        dense_shape=result.shape,
    )


def recursion_tensor(l: int, dtype: Union[Type, str] = tf.float32) -> TFArray:
    if l == 0:
        return initial(dtype)
    return cast(
        TFArray,
        tf.linalg.matmul(
            inner_recursion_tensor(l, dtype), outer_recursion_tensor(l, dtype)
        ),
    )


def sparse_recursion_tensor(l: int, dtype: Union[Type, str] = tf.float32) -> TFArray:
    if l == 0:
        return initial(dtype)
    return cast(
        TFArray,
        tf.linalg.matmul(
            inner_recursion_sparse(l, dtype), outer_recursion_sparse(l, dtype)
        ),
    )


def initial(dtype: Union[Type, str] = tf.float32) -> TFArray:
    """Start of the recursion."""

    return tf.constant([[1]], dtype=dtype)


def full_tensor(
    compressed: Array,
    lmin: int = 0,
    lmax: Optional[int] = None,
    dtype: Optional[Union[Type, str]] = None,
) -> TFArray:
    """Converts compressed tensors to the full 2L by 2L tensor.

    More explicitly, it creates a tensor where all m, m' components are present where
    :math:`l_{\\min} \\leq |m| \\leq l_{\\max}`.

    compressed sensor needs not correspond to an L within that range. The resulting
    tensor will be padded with zeros for out-of-range values.
    """
    from copy import deepcopy
    from itertools import chain
    from typing import Iterable

    L = order_from_ncoeffs(len(compressed))

    lmax = lmax or L
    dtype = dtype or compressed.dtype
    if lmin <= 0:
        N = 2 * lmax + 1
        iterator: Iterable = range(-lmax, lmax + 1)
    else:
        N = 2 * (lmax - lmin + 1)
        iterator = chain(range(-lmax, -lmin + 1), range(lmin, lmax + 1))
    result = np.zeros((N, N), dtype=getattr(dtype, "as_numpy_dtype", dtype))
    for m in deepcopy(iterator):
        for mp in deepcopy(iterator):
            index, factor = symmetrized_index(L, m, mp)
            result[m + lmax, mp + lmax] = compressed[index] * factor
    return tf.constant(result, dtype=dtype)


def straightforward(
    l: int,
    m1: int,
    m2: int,
    sqrts: Optional[Array] = None,
) -> float:
    """Straightforward implementation of the Trapani recuurence."""
    if m1 < -l or m1 > l or m2 < -l or m2 > l:
        return 0
    elif l == 0:
        return 1

    if sqrts is None:
        sqrts = np.sqrt(np.arange(4 * l + 1))
    assert sqrts is not None

    if m1 < 0 and m2 < 0:
        return straightforward(l, -m2, -m1, sqrts)
    elif m1 < 0:
        result = straightforward(l, -m1, m2, sqrts)
        return result if (l - m2) % 2 == 0 else -result
    elif m2 < 0:
        result = straightforward(l, m1, -m2, sqrts)
        return result if (l - m1) % 2 == 0 else -result
    elif m2 < m1:
        result = straightforward(l, m2, m1, sqrts)
        return result if (m1 - m2) % 2 == 0 else -result
    elif l == m1:
        return (
            sqrts[l]
            * sqrts[2 * l - 1]
            / (sqrts[2 * (l + m2)] * sqrts[l + m2 - 1])
            * straightforward(l - 1, l - 1, m2 - 1, sqrts)
        )
    return (
        2
        * m2
        / (sqrts[l - m1] * sqrts[l + m1 + 1])
        * straightforward(l, m1 + 1, m2, sqrts)
    ) - (
        sqrts[l - m1 - 1]
        * sqrts[l + m1 + 2]
        / (sqrts[l - m1] * sqrts[l + m1 + 1])
        * straightforward(l, m1 + 2, m2, sqrts)
    )


def deltas(
    *,
    labels: Optional[Array] = None,
    lmax: Optional[int] = None,
    lmin: int = 0,
    mmin: Optional[int] = None,
    mmax: Optional[int] = None,
    mpmin: Optional[int] = None,
    mpmax: Optional[int] = None,
    scaled: bool = True,
    dtype: Union[str, tf.DType, np.dtype] = tf.float32,
) -> TFArray:
    f"""Wigner-d at pi / 2 via the Trapani, Navaza recurrence.

    See [Trapani, Navaza (2006)]

    {REFERENCES['TN']}

    Example:

        We can check the recurrence works against the naive, brute-force implementation:

        >>> from pytest import approx
        >>> from tensossht import wignerd_labels
        >>> from tensossht.specialfunctions.naive import wignerd
        >>> from tensossht.specialfunctions.trapani import deltas
        >>> labels = wignerd_labels(lmax=8)
        >>> lmmp = deltas(labels=labels, dtype=tf.float64)
        >>> expected = [wignerd(*labels[:, i].numpy()) for i in range(labels.shape[1])]
        >>> lmmp.numpy() == approx(expected)
        True

        Equivalently, we could also give as input `lmax` and friends, rather than a
        vector of labels:

        >>> lmmp.numpy() == approx(deltas(lmax=8, dtype=tf.float64).numpy())
        True

        Note that this function only accepts keyword arguments.
    """
    from tensossht.sampling import wignerd_labels

    if not scaled:
        raise NotImplementedError

    if labels is None and lmax is None:
        raise ValueError("Missing on of labels or (lmax, lmin...)")
    if labels is None:
        assert isinstance(lmax, int)
        labels_ = wignerd_labels(
            lmax=lmax, lmin=lmin, mmin=mmin, mmax=mmax, mpmin=mpmin, mpmax=mpmax
        )
    else:
        labels_ = tf.convert_to_tensor(labels)
        lmax = tf.reduce_max(labels[0])

    assert lmax is not None
    sqrts = tf.sqrt(tf.range(tf.cast(2 * (lmax + 1) + 1, dtype=dtype)))
    assert labels_ is not None
    return cast(TFArray, _deltas_impl(labels_, sqrts=sqrts, lmax=lmax))


@tf.function
def _deltas_impl(labels: Array, sqrts: Array, lmax: Union[int, Array]) -> TFArray:
    from tensossht.sampling import symmetric_labels

    symlabs, factors = symmetric_labels(labels, dtype=sqrts.dtype)

    ll0 = _delta_ll0_impl(
        tf.maximum(symlabs[0] - symlabs[2], 0),
        dtype=sqrts.dtype,
        sqrts=sqrts[1 : 2 * lmax + 1],
    )
    llm = _delta_llm_impl(symlabs[0], symlabs[2], ll0, sqrts)

    return _delta_lmmp_impl(symlabs, llm, sqrts) * factors


def delta_ll0(
    llabels: tf.Tensor,
    lmax: Optional[int] = None,
    sqrts: Optional[tf.Tensor] = None,
    dtype: Union[str, tf.DType, np.dtype] = tf.float32,
) -> TFArray:
    f"""Equation 9 of the pyramid.

    See [Trapani, Navaza (2006)]

    {REFERENCES['TN']}

    Example:

        >>> from tensossht.specialfunctions.trapani import delta_ll0
        >>> labels = tf.range(5)
        >>> delta_ll0(labels, dtype=tf.float64).numpy()
        array([ 1.        , -0.70710678,  0.61237244, -0.55901699,  0.52291252])

    """
    if lmax is None:
        lmax = tf.reduce_max(llabels)
        assert lmax is not None
    if sqrts is None:
        sqrts_: TFArray = tf.sqrt(tf.range(1, tf.cast(2 * lmax + 1, dtype=dtype)))
    else:
        sqrts_ = sqrts[1 : (2 * lmax + 1)]  # type: ignore
    return cast(TFArray, _delta_ll0_impl(llabels, sqrts_, dtype))


@tf.function
def _delta_ll0_impl(
    llabels: Array,
    sqrts: Array,
    dtype: Union[str, tf.DType, np.dtype] = tf.float32,
) -> TFArray:
    values = tf.pad(
        tf.scan(
            lambda head, rest: -head * rest,
            sqrts[:-1:2] / sqrts[1::2],
            tf.cast(1, dtype=dtype),
        ),
        ((1, 0),),
        constant_values=tf.constant(1, dtype=dtype),
    )
    return tf.gather(values, llabels, axis=0)


def delta_llm(
    llabels: Array,
    mlabels: Array,
    initial: Optional[Array] = None,
    sqrts: Optional[Array] = None,
    dtype: Union[str, tf.DType, np.dtype] = tf.float32,
) -> TFArray:
    f"""Computes wigner-d (l, m, m') for m = l and any m', at beta = pi / 2.

    Applies equations 10 (and optionally, 9) of the pyramid in [Taprani, Navaza (2006)].

    {REFERENCES['TN']}

    Example:

        Let's first create `llabels` and `mlables` for all (l, l, m) triplets. We do
        this by first generating all labels using
        :py:func:`tensossht.specialfunctions.wignerd_labels`, and then removing those
        where `m != l`.

        >>> from tensossht import wignerd_labels
        >>> labels = wignerd_labels(8)
        >>> labels = tf.boolean_mask(labels[::2], labels[0] == labels[1], axis=1)

        Now we can call :py:func:`delta_llm` and compare to the naive, brute-force
        implementation with multi-precision floating points:

        >>> from pytest import approx
        >>> from tensossht.specialfunctions.naive import wignerd
        >>> from tensossht.specialfunctions.trapani import delta_llm
        >>> result = delta_llm(labels[0], labels[1], dtype=tf.float64)
        >>> expected = [float(wignerd(l, l, m)) for l, m in zip(*labels.numpy())]
        >>> result.numpy() == approx(expected)
        True

    """
    mlabels = tf.abs(mlabels)
    if sqrts is None:
        lmax = tf.reduce_max(llabels)
        sqrts = tf.sqrt(tf.range(tf.cast(2 * (lmax + 1), dtype)))
    assert sqrts is not None
    if initial is None:
        lmax = tf.reduce_max(llabels)
        initial = _delta_ll0_impl(
            tf.maximum(llabels - mlabels, 0),
            sqrts=sqrts[1 : 2 * lmax + 1],
            dtype=dtype,
        )
    return _delta_llm_impl(llabels, mlabels, initial, sqrts)


@tf.function
def _delta_llm_impl(
    llabels: Array, mlabels: Array, initial: Array, sqrts: Array
) -> TFArray:
    result = initial
    ls = llabels - mlabels + cast(TFArray, 1)
    ms = tf.ones_like(mlabels)

    dowork = tf.logical_and(mlabels != 0, llabels > 0)
    condition = tf.logical_and(ms <= mlabels, dowork)
    for _ in tf.range(tf.reduce_max(tf.where(dowork, mlabels - ms, 0)) + 1):
        result = tf.where(
            condition,
            tf.gather(sqrts, ls)
            * tf.gather(sqrts, tf.math.maximum(2 * ls - 1, 0))
            / (
                tf.gather(sqrts, ls + ms)
                * tf.gather(sqrts, tf.math.maximum(ls + ms - 1, 0))
                * sqrts[2]
            )
            * result,
            result,
        )
        ms = tf.where(condition, ms + 1, ms)
        ls = tf.where(condition, ls + 1, ls)
        condition = tf.logical_and(ms <= mlabels, dowork)

    return tf.where(
        tf.logical_and(llabels >= mlabels, mlabels >= -llabels),
        result,
        tf.constant(0, dtype=result.dtype),
    )


@tf.function
def _delta_lmmp_impl(labels: Array, initial: Array, sqrts: Array) -> TFArray:
    """Implements Eq 11 of the Trapani recurrence pyramid.

    Example:

        First, we ensure the recurrence does not act on (l, l, m) terms

        >>> from pytest import approx
        >>> from tensossht import wignerd_labels
        >>> from tensossht.specialfunctions.trapani import _delta_lmmp_impl, delta_llm
        >>> labels = wignerd_labels(8)
        >>> labels = tf.boolean_mask(labels, labels[0] == labels[1], axis=1)
        >>> llm = delta_llm(labels[0], labels[2], dtype=tf.float64)
        >>> sqrts = tf.sqrt(tf.range(2 * labels.shape[1] + 2, dtype=tf.float64))
        >>> lmmp = _delta_lmmp_impl(labels, llm, sqrts)
        >>> lmmp.numpy() == approx(llm.numpy())
        True

        Now we check the recurrence with only one term against the naive,
        multi-precision implementation:

        >>> from tensossht.specialfunctions.naive import wignerd
        >>> labels = wignerd_labels(8)
        >>> labels = tf.boolean_mask(labels, labels[0] == labels[1] + 1, axis=1)
        >>> llm = delta_llm(labels[0], labels[2], dtype=tf.float64)
        >>> lmmp = _delta_lmmp_impl(labels, llm, sqrts)
        >>> expected = [wignerd(*labels[:, i].numpy()) for i in range(labels.shape[1])]
        >>> lmmp.numpy() == approx(expected)
        True

        Finally, we check the full recurrence:

        >>> labels = wignerd_labels(8)
        >>> llm = delta_llm(labels[0], labels[2], dtype=tf.float64)
        >>> lmmp = _delta_lmmp_impl(labels, llm, sqrts)
        >>> expected = [wignerd(*labels[:, i].numpy()) for i in range(labels.shape[1])]
        >>> lmmp.numpy() == approx(expected)
        True

    """
    mp_fac = tf.cast(2 * labels[2], dtype=initial.dtype)
    ms = labels[0]
    condition = ms > labels[1]
    denom = tf.gather(sqrts, labels[0] - ms + 1) * tf.gather(sqrts, labels[0] + ms)
    result = tf.where(condition, mp_fac / denom * initial, initial)
    upper = initial

    ms = tf.where(condition, ms - 1, ms)
    condition = ms > labels[1]
    for _ in tf.range(tf.reduce_max(ms - labels[1])):
        denom = tf.gather(sqrts, labels[0] - ms + 1) * tf.gather(sqrts, labels[0] + ms)
        mid = result
        result = tf.where(
            condition,
            mp_fac / denom * mid
            - tf.gather(sqrts, labels[0] - ms)
            * tf.gather(sqrts, labels[0] + ms + 1)
            * upper
            / denom,
            result,
        )
        upper = mid
        ms = tf.where(condition, ms - 1, ms)
        condition = ms > labels[1]

    return tf.where(
        tf.logical_and(
            tf.logical_and(labels[0] >= labels[1], labels[1] >= -labels[0]),
            tf.logical_and(labels[0] >= labels[2], labels[2] >= -labels[0]),
        ),
        result,
        tf.constant(0, dtype=result.dtype),
    )
