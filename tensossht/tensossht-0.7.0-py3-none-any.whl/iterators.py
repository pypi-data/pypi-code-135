"""Iterators that simplify summations in the spherical transforms."""
from __future__ import annotations

from typing import Iterator, Optional, Tuple, Union, cast

import numpy as np
import tensorflow as tf

from tensossht.sampling import HarmonicSampling
from tensossht.typing import Array, TFArray

TRAPANI_ITERATOR_STATE = Tuple[TFArray, TFArray, TFArray]
SUM_ITERATOR_STATE = Tuple[TRAPANI_ITERATOR_STATE, TRAPANI_ITERATOR_STATE]


class TrapaniIterator:
    """Iteration object of Delta_{mm'}^l over m.

    Since tensorflow's authograph does not understand generators or loops, this is a
    cruder iterator that still simplifies looping over Delta_mm'^l.
    In any case, it means we only need store :math:`O(l^2)` components, rather than
    :math:`O(l^3)`.

    Example:

        It is simpler to create these objects via the factory function. The latter can
        take as argument either a fully formed 2 by n `labels` array, or it will create
        one by passing its arguments to
        :py:func:`~tensossht.specialfunctions.wignerd_labels`:

        >>> from pytest import approx
        >>> from tensossht import wignerd_labels
        >>> from tensossht.iterators import TrapaniIterator
        >>> from tensossht.specialfunctions.naive import wignerd
        >>> lmax = 8
        >>> labels = wignerd_labels(lmax=lmax, mmax=0, mmin=0, mpmax=lmax, mpmin=0)
        >>> iterator = TrapaniIterator.factory(
        ...     lmax=lmax, mmin=0, mmax=0, mpmax=lmax, mpmin=0, dtype=tf.float64
        ... )
        >>> assert tf.reduce_all(iterator.llabels == labels[0])

        At each turn of the clock, only the `m=l - i` are available.

        >>> for actual, m in zip(iterator, range(lmax - 1, -1, -1)):
        ...     expected = np.array(
        ...         [float(wignerd(l, m, mp)) for (l, mp) in labels[::2].numpy().T]
        ...     )
        ...     assert actual.numpy() == approx(expected)

        Once the iteration is done, in other words once all `m` comonents are equal to
        zero, the iterator keeps on returning returning zeros, rather than signal that
        the iteration has ended. This is because of the underlying limitations of
        tensorflow:

        >>> assert next(iterator).numpy() == approx(0)
        >>> assert next(iterator).numpy() == approx(0)
        >>> assert next(iterator).numpy() == approx(0)

        When the fun stops, stop.
    """

    @classmethod
    def factory(
        cls,
        *,
        labels: Optional[TFArray] = None,
        lmax: Optional[int] = None,
        lmin: int = 0,
        mmin: Optional[int] = None,
        mmax: Optional[int] = None,
        mpmin: Optional[int] = None,
        mpmax: Optional[int] = None,
        dtype: Union[str, tf.DType, np.dtype] = tf.float32,
    ):
        from tensossht.sampling import wignerd_labels
        from tensossht.specialfunctions.trapani import delta_llm

        if labels is None and lmax is None:
            raise ValueError("Missing on of labels or (lmax, lmin...)")
        if labels is None:
            assert isinstance(lmax, int)
            labels = wignerd_labels(
                lmax=lmax, lmin=lmin, mmin=mmin, mmax=mmax, mpmin=mpmin, mpmax=mpmax
            )
        else:
            lmax = tf.reduce_max(labels[0]) + 1
        assert lmax is not None and labels is not None
        rdtype = tf.dtypes.as_dtype(dtype).real_dtype
        sqrts = tf.sqrt(tf.range(2 * lmax + 1, dtype=rdtype))
        llm = delta_llm(labels[0], labels[-1], sqrts=sqrts, dtype=rdtype)

        return cls(labels[::2], llm, sqrts)

    def __init__(self, labels: TFArray, llm: TFArray, sqrts: TFArray):
        self.llabels = labels[0]
        self.mlabels = labels[1]
        self._sqrts = sqrts
        self._numerator = tf.cast(2 * self.mlabels, dtype=llm.dtype)
        self.lmax = tf.reduce_max(self.llabels) + 1

        self.reset(llm)

    @property
    def shape(self):
        return self._current.shape

    @property
    def dtype(self):
        return self._current.dtype

    def reset(self, llm: TFArray):
        self._m = self.lmax
        self._current = tf.where(self.llabels >= tf.abs(self.mlabels), llm, 0)
        self._upper = self._current

    def __next__(self) -> TFArray:
        result, (self._m, self._current, self._upper) = cast(
            Tuple[TFArray, TRAPANI_ITERATOR_STATE], self.tf_next(self.tf_state)
        )
        return result

    def __iter__(self):
        return self

    def _post(
        self, m: TFArray, current: TFArray
    ) -> Tuple[TFArray, TRAPANI_ITERATOR_STATE]:
        zero = tf.zeros_like(current)
        return zero, (m, zero, zero)

    def _iterate(self, m, current, upper) -> Tuple[TFArray, TFArray]:
        condition = self.llabels >= tf.abs(m)
        mid = current
        current = tf.where(
            condition,
            (
                self._numerator * current
                - tf.gather(self._sqrts, tf.maximum(self.llabels - m, 0))
                * tf.gather(self._sqrts, tf.maximum(self.llabels + m + 1, 0))
                * upper
            )
            / (
                tf.gather(self._sqrts, tf.maximum(self.llabels - m + 1, 0))
                * tf.gather(self._sqrts, tf.maximum(self.llabels + m, 0))
            ),
            current,
        )
        return current, mid

    @tf.function
    def tf_next(
        self, state: TRAPANI_ITERATOR_STATE
    ) -> Tuple[TFArray, TRAPANI_ITERATOR_STATE]:
        m, current, upper = state
        if m <= 0:
            return self._post(m, current)

        if m < self.lmax:
            current, upper = self._iterate(m, current, upper)

        result = tf.where(
            self.llabels + 2 <= m, tf.constant(0, dtype=current.dtype), current
        )
        return result, (m - 1, current, upper)

    @property
    def tf_state(self) -> TRAPANI_ITERATOR_STATE:
        return self._m, self._current, self._upper


class DeltaDeltaIterator:
    r"""Iterator over :math:`m'` yielding :math`\Delta_{l,m',m} * \Delta_{l, m',-s}`."""

    def __init__(
        self,
        labels: TFArray,
        llm: TFArray,
        lls: TFArray,
        sqrts: TFArray,
        lls_shape: Optional[Union[Tuple, tf.TensorShape]] = None,
    ):
        if len(labels.shape) != 2:
            raise ValueError("Labels ought to be a 2d matrix")
        if labels.shape[0] not in (2, 3):
            msg = "Labels ought to be a 2 by n matrix (no spin) or a 3 by n matrix."
            raise ValueError(msg)
        if llm.dtype != lls.dtype:
            raise ValueError("llm and lls sgould have the same dtype")
        if llm.dtype not in {tf.float32, tf.float64}:
            raise ValueError("llm and lls must be float32 or float64")
        if llm.shape[0] != lls.shape[0] and lls_shape is None:
            assert lls.shape[0] % llm.shape[0] == 0
            lls_shape = lls.shape[0] // llm.shape[0], llm.shape[0]

        self.llm = llm
        """Cached initial llm."""
        self.lls = lls
        """Cached initial lls."""
        if labels.shape[0] == 2:
            slabels = tf.zeros_like(labels[0:1])
        else:
            slabels = tf.where(
                tf.abs(labels[2:3]) > labels[:1], labels[:1] + 1, -labels[2:3]
            )
        self.iter_s = TrapaniIterator(
            tf.concat((labels[0:1], slabels), axis=0), self.lls, sqrts
        )
        """Iterator over :math:`\\Delta_{l,m',-s}`."""
        self.iter_m = TrapaniIterator(labels[:2, : len(self.llm)], llm, sqrts)
        """Iterator over :math:`\\Delta_{l,m',m}`."""
        if lls_shape is not None:
            lls_shape = tuple(lls_shape)
        self.lls_shape = lls_shape

    @classmethod
    def factory(
        cls,
        hsampling: Union[HarmonicSampling, TFArray, int],
        sqrts: Optional[TFArray] = None,
        lls_shape: Optional[Union[Tuple, tf.TensorShape]] = None,
        dtype: Union[str, np.dtype, tf.DType] = tf.float32,
    ):
        from tensossht.sampling import harmonic_sampling_scheme
        from tensossht.specialfunctions.trapani import deltas

        if not isinstance(hsampling, HarmonicSampling):
            hsampling = harmonic_sampling_scheme(hsampling)
        rdtype = tf.dtypes.as_dtype(dtype).real_dtype

        if hsampling.is_multi_spin and hsampling.is_separable_spin:
            llm_labels = tf.reshape(hsampling.labels, (3, hsampling.nspins, -1))[:, 0]
        else:
            llm_labels = hsampling.labels
        llm_mlabels = tf.math.minimum(llm_labels[:1], hsampling.mmax)
        llm = deltas(
            labels=tf.concat((llm_labels[:1], llm_mlabels, llm_labels[1:2]), axis=0),
            dtype=rdtype,
        )

        # where spin is out of range, make m out of range
        # where spin is in-range set m to l or mmax.
        lls_mlabels = tf.where(
            tf.abs(hsampling.labels[2:3]) > hsampling.labels[:1],
            hsampling.labels[:1] + 1,
            tf.math.minimum(hsampling.labels[:1], hsampling.mmax),
        )
        spin_labels = (
            tf.fill(
                (1, hsampling.labels.shape[1]), tf.cast(0, dtype=hsampling.labels.dtype)
            )
            if hsampling.labels.shape[0] == 2
            else -hsampling.labels[2:3]
        )
        lls = deltas(
            labels=tf.concat((hsampling.labels[:1], lls_mlabels, spin_labels), axis=0),
            dtype=rdtype,
        )
        if sqrts is None:
            sqrts = tf.sqrt(
                tf.cast(tf.range(2 * (hsampling.lmax + 1) + 1), dtype=llm.dtype)
            )
        assert sqrts is not None
        return cls(hsampling.labels, llm, lls, sqrts=sqrts, lls_shape=lls_shape)

    @property
    def tf_state(self) -> SUM_ITERATOR_STATE:
        return self.iter_m.tf_state, self.iter_s.tf_state

    def reset(self):
        self.iter_m.reset(self.llm)
        self.iter_s.reset(self.lls)

    @tf.function
    def next(self, state: SUM_ITERATOR_STATE) -> Tuple[TFArray, SUM_ITERATOR_STATE]:
        iterm_result, iterm_state = cast(
            Tuple[TFArray, TRAPANI_ITERATOR_STATE], self.iter_m.tf_next(state[0])
        )
        iters_result, iters_state = cast(
            Tuple[TFArray, TRAPANI_ITERATOR_STATE], self.iter_s.tf_next(state[1])
        )

        if self.lls_shape is not None:
            iters_result = tf.reshape(iters_result, self.lls_shape)
        return iterm_result * iters_result, (iterm_state, iters_state)


def sign_condition(hsampling: Union[TFArray, HarmonicSampling, int]) -> TFArray:
    from tensossht.sampling import harmonic_sampling_scheme

    if not isinstance(hsampling, HarmonicSampling):
        hsampling = harmonic_sampling_scheme(hsampling)
    if hsampling.is_multi_spin and hsampling.is_separable_spin:
        mlabels = tf.reshape(hsampling.labels[1], (hsampling.nspins, -1))[:1]
        slabels = tf.reshape(hsampling.labels[2], (hsampling.nspins, -1))
    else:
        mlabels = hsampling.labels[1]
        slabels = hsampling.labels[2]
    return (mlabels + slabels) % 2 == 0


class LIterator(Iterator):
    """Iterator over :math:`l'` yielding :math`\\Delta_{l,m,m'}`.

    The iterator returns a subset of values for :math:`l >= m >= m' >= 0` as follows:

        1. :math:`\\Delta_{l=0, m=0, m'=0}`
        2. :math:`\\Delta_{1, 0, 0}`, :math:`\\Delta_{1, 1, 0}`,
           :math:`\\Delta_{1, 1, 1}`
        2. :math:`\\Delta_{2, 0, 0}`, :math:`\\Delta_{2, 1, 0}`,
           :math:`\\Delta_{2, 1, 1}`,:math:`\\Delta_{2, 2, 0}`,
           :math:`\\Delta_{2, 2, 1}`, :math:`\\Delta_{2, 2, 2}`,

    Other values can be obtained by symmetry. The iterator stops when `max_degee` is
    reached (excluded). If `max_degree = None`, then the iterator does not stop. The
    full symmetric matrix can be obtained with :py:func:`LIterator.symmetrize`.

    Example:
        >>> from pytest import approx
        >>> from tensossht.iterators import LIterator
        >>> from tensossht.specialfunctions.trapani import straightforward
        >>> def expected(degree):
        ...     return [
        ...         straightforward(degree, m1, m2)
        ...         for m1 in range(0, degree + 1)
        ...         for m2 in range(0, m1 + 1)
        ...     ]
        >>> for degree, actual in enumerate(LIterator(max_degree=11, dtype=tf.float64)):
        ...     assert np.array(actual) == approx(expected(degree))

    """

    def __init__(
        self, max_degree: Optional[int] = None, dtype: tf.DType = tf.dtypes.float32
    ):
        self._dtype = dtype
        self._degree: int = 0
        self._ll0: Array = tf.constant(1, dtype=self.dtype)
        self._llm: Array = tf.constant([], dtype=self.dtype)
        self._max_degree = max_degree

    @property
    def dtype(self) -> tf.DType:
        return self._dtype

    @property
    def degree(self) -> int:
        """Degree of the *next* iteration"""
        return self._degree

    def _next_ll0(self, degree: int) -> TFArray:
        """Update ll0 and degree"""
        self._ll0 = -self._ll0 * self._ll0_coeff(degree, self.dtype)
        return self._ll0

    def _next_llm(self, degree: int, previous_ll0: TFArray) -> TFArray:
        """Update llm, ll0, and degree"""
        self._llm = cast(
            TFArray,
            tf.concat((previous_ll0[None], self._llm), axis=0)
            * self._llm_coeffs(degree, self.dtype),
        )
        return self._llm

    def _next_lmpm(self, degree: int, ll0: TFArray, llm: TFArray) -> TFArray:
        coeffs = self._lmpm_coeffs(degree, self.dtype)
        mp1_values = tf.concat((ll0[None], llm[:-1]), axis=0)
        mp2_values = tf.zeros(tf.shape(mp1_values)[0], self.dtype)
        result: list[TFArray] = []
        index = 0
        for m1 in range(degree - 1, -1, -1):
            mp1_coeffs = coeffs[0, index : index + m1 + 1]
            mp2_coeffs = coeffs[1, index : index + m1 + 1]
            result.insert(0, mp1_coeffs * mp1_values + mp2_coeffs * mp2_values)
            mp2_values = mp1_values[:-1]
            mp1_values = result[0][:-1]
            index += m1 + 1
        return cast(TFArray, tf.concat(result, axis=0))

    @staticmethod
    def _ll0_coeff(degree: int, dtype: tf.DType = tf.dtypes.float32) -> TFArray:
        inv_two_l = 1 / tf.constant(2 * degree, dtype=dtype)
        return tf.sqrt(1 - inv_two_l)

    @staticmethod
    def _llm_coeffs(degree: int, dtype: tf.DType = tf.dtypes.float32) -> TFArray:
        return tf.sqrt(
            tf.constant(degree * (2 * degree - 1), dtype=dtype)
            / tf.cast(
                2 * tf.range(degree + 1, 2 * degree + 1) * tf.range(degree, 2 * degree),
                dtype=dtype,
            )
        )

    @staticmethod
    def _mlabels(degree: int, dtype: tf.DType = tf.dtypes.int16) -> TFArray:
        return tf.constant(
            [(m, mp) for m in range(degree - 1, -1, -1) for mp in range(0, m + 1)],
            dtype=dtype,
        )

    @staticmethod
    def _lmpm_coeffs(degree: int, dtype: tf.DType = tf.dtypes.float32) -> TFArray:
        labels = LIterator._mlabels(degree)
        m1 = labels[:, 0]
        m2 = labels[:, 1]

        denom = 1 / cast(
            TFArray, tf.cast((degree - m1) * (degree + m1 + 1), dtype=dtype)
        )
        mp1 = cast(TFArray, tf.cast(2 * m2, dtype)) * tf.sqrt(denom)
        mp2 = -tf.sqrt(
            cast(TFArray, tf.cast((degree - m1 - 1) * (degree + m1 + 2), dtype=dtype))
            * denom
        )
        return cast(TFArray, tf.stack((mp1, mp2)))

    def __iter__(self) -> LIterator:
        return self

    def __next__(self) -> TFArray:
        if self._max_degree is not None and self._degree >= self._max_degree:
            raise StopIteration()
        self._degree += 1
        if self._degree == 1:
            return self._ll0[None]
        previous_ll0 = self._ll0
        self._ll0 = self._next_ll0(self._degree - 1)
        self._llm = self._next_llm(self._degree - 1, previous_ll0)
        lmpm = self._next_lmpm(self._degree - 1, self._ll0, self._llm)
        return tf.concat((lmpm, self._ll0[None], self._llm), axis=0)

    @staticmethod
    def symmetrize(degree: int, coeffs: TFArray) -> TFArray:
        """Transforms symmetric wigner-d :math:`m' >= m >= 0` to full :math:(m, m'):"""
        if degree == 0:
            return coeffs[None, :]
        ragged = tf.RaggedTensor.from_row_lengths(
            coeffs, tf.range(1, degree + 2), validate=False
        )
        upper_triangular = tf.transpose(ragged.to_tensor())

        m = tf.range(degree + 1)
        lower_triangular = tf.transpose(
            tf.where((m[:, None] - m) % 2 == 0, upper_triangular, -upper_triangular)
        )

        lr_quad = tf.where(m > m[:, None], upper_triangular, lower_triangular)
        ll_quad_impl = lr_quad[:, -1 : -lr_quad.shape[-1] : -1]
        ll_quad = tf.where((degree - m[:, None]) % 2 == 0, ll_quad_impl, -ll_quad_impl)
        l_quads = tf.concat((ll_quad, lr_quad), axis=1)
        u_quads_impl = l_quads[-1 : -l_quads.shape[0] : -1]
        u_quads = tf.where(
            (degree - tf.range(-degree, degree + 1)) % 2 == 0,
            u_quads_impl,
            -u_quads_impl,
        )

        return tf.concat((u_quads, l_quads), axis=0)


class LDeltaDeltaIterator(LIterator):
    r"""Iterator over :math:`l'` yielding :math`\Delta_{l,m',m} * \Delta_{l, m',-s}`."""

    def __init__(
        self,
        spin: int = 0,
        max_degree: Optional[int] = None,
        dtype: tf.DType = tf.dtypes.float32,
    ):
        super().__init__(max_degree=max_degree, dtype=dtype)
        self.spin = spin

    def __next__(self):
        if self._max_degree is not None and self._degree >= self._max_degree:
            raise StopIteration()
        self._degree += 1
        if self._degree == 1:
            if self.spin == 0:
                return self._ll0[None]
            return next(self)
        previous_ll0 = self._ll0
        self._ll0 = self._next_ll0(self._degree - 1)
        self._llm = self._next_llm(self._degree - 1, previous_ll0)
        if abs(self.spin) >= self.degree:
            return next(self)
        llmspin = self._ll0 if self.spin == 0 else self._llm[abs(self.spin) - 1]
        ll0_lls = self._ll0 * llmspin
        llm_lls = self._llm * llmspin
        lmpm = self._next_lmpm_lmpmspin(self._degree - 1, self._ll0, self._llm)
        return tf.concat((lmpm, ll0_lls[None], llm_lls), axis=0)

    def _next_lmpm_lmpmspin(self, degree: int, ll0: TFArray, llm: TFArray) -> TFArray:
        coeffs = self._lmpm_coeffs(degree, self.dtype)
        result: list[TFArray] = []
        delta_spin = tf.concat((ll0[None], llm), axis=0)
        mp1_values = delta_spin[:-1]
        mp2_values = tf.zeros(tf.shape(mp1_values)[0], self.dtype)
        index = 0
        for m1 in range(degree - 1, -1, -1):
            mp1_coeffs = coeffs[0, index : index + m1 + 1]
            mp2_coeffs = coeffs[1, index : index + m1 + 1]
            current = mp1_coeffs * mp1_values + mp2_coeffs * mp2_values
            if self.spin > 0 and self.spin < m1:
                factor = (2 * ((self.degree - m1) % 2) - 1) * current[self.spin]
            elif self.spin > 0 and self.spin == m1:
                delta_spin = current
                factor = (2 * ((self.degree - self.spin) % 2) - 1) * delta_spin[m1]
            elif self.spin > 0:
                factor = (2 * ((self.degree - self.spin) % 2) - 1) * delta_spin[m1]
            elif self.spin == 0:
                factor = current[-self.spin]
            elif -self.spin < m1:
                factor = current[-self.spin]
            elif -self.spin == m1:
                delta_spin = current
                factor = delta_spin[m1]
            else:
                factor = -(2 * ((self.spin - m1) % 2) - 1) * delta_spin[m1]
            result.insert(0, current * factor)
            mp2_values = mp1_values[:-1]
            mp1_values = current[:-1]
            index += m1 + 1
        return cast(TFArray, tf.concat(result, axis=0))
