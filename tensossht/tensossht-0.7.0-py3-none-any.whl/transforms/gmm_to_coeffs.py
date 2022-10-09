from typing import Optional, Tuple, Union

import numpy as np
import tensorflow as tf

from tensossht.iterators import SUM_ITERATOR_STATE, DeltaDeltaIterator
from tensossht.references import REFERENCES
from tensossht.sampling import HarmonicSampling


class GmmToCoeffs:
    f"""Performs summation from Gmm to flm.

    See equation 9 of [McEwen, Wiaux (2011)] (except it rolls together the factors
    :math:`2\\pi` from 9 and 19).

    Assumes Gmm is for a complex signal, i.e. :math:`m \\in [-l, l]`.


    {REFERENCES['MW']}
    """

    def __init__(
        self,
        hsampling: Union[tf.Tensor, HarmonicSampling, int],
        factor: Optional[tf.Tensor] = None,
        deltadelta_iterator: Optional[DeltaDeltaIterator] = None,
        dtype: Union[str, np.dtype, tf.DType] = tf.float32,
    ):
        from tensossht.iterators import sign_condition
        from tensossht.sampling import harmonic_sampling_scheme

        if not isinstance(hsampling, HarmonicSampling):
            hsampling = harmonic_sampling_scheme(hsampling)

        self.lmax = hsampling.lmax
        """Minimum order for the transform."""
        if hsampling.is_multi_spin and hsampling.is_separable_spin:
            self.mlabels = tf.reshape(hsampling.labels[1], (hsampling.nspins, -1))[0]
        else:
            self.mlabels = hsampling.labels[1]
        """Cached initial lls."""
        if factor is None:
            factor = gmm_factor(hsampling, dtype=dtype)
        self.factor = factor
        r"""Final factor:

        .. math:

            (-1)^s\imath^{s+m}\sqrt\left(\frac{2l + 1}{4\pi}\right)
        """
        if deltadelta_iterator is None:
            deltadelta_iterator = DeltaDeltaIterator.factory(
                hsampling.labels, dtype=dtype
            )
        self.deltadelta_iterator = deltadelta_iterator
        """Iterator over Delta * Delta coeffs"""
        self.sign_condition = sign_condition(hsampling)

    def reset(self):
        """Resets iterators."""
        self.deltadelta_iterator.reset()

    def indices(self, m: int):
        offseted_m = tf.expand_dims(self.mlabels, 1)
        return tf.concat((offseted_m, tf.fill(offseted_m.shape, m)), 1) + self.lmax - 1

    def _next(
        self, mp: tf.Tensor, gmmT: tf.Tensor, iter_state: SUM_ITERATOR_STATE
    ) -> Tuple:
        perm = tf.range(1, len(gmmT.shape)) % (len(gmmT.shape) - 1)
        gmm_plus = tf.transpose(tf.gather_nd(gmmT, self.indices(mp)), perm)
        # g^T_{-m', m}
        gmm_minus = tf.transpose(tf.gather_nd(gmmT, self.indices(-mp)), perm)
        # g^T_{m', m} + g^T_{-m', m} * sign + axis manipulation
        gmm_summand = gmm_plus + tf.where(self.sign_condition, gmm_minus, -gmm_minus)
        deltadelta, iter_state = self.deltadelta_iterator.next(iter_state)
        return (
            iter_state,
            (
                tf.cast(deltadelta, dtype=gmmT.dtype)
                # avoid double counting when  m' == 0
                * (gmm_plus if mp == 0 else gmm_summand)
            ),
        )

    @tf.function
    def __call__(self, gmm: tf.Tensor) -> tf.Tensor:
        assert self.factor is not None
        self.reset()
        iter_state = self.deltadelta_iterator.tf_state
        # Axis manipulations to simplify gather and summation itself.
        gmmT = tf.transpose(
            gmm,
            perm=[len(gmm.shape) - 2, len(gmm.shape) - 1]
            + [i for i in range(len(gmm.shape) - 2)],
        )
        iter_state, result = self._next(self.lmax - 1, gmmT, iter_state)
        for mp in tf.range(self.lmax - 2, -1, -1):
            iter_state, iteration = self._next(mp, gmmT, iter_state)
            result += iteration

        return tf.cast(result, self.factor.dtype) * self.factor


def many_spins_factor(labels: tf.Tensor, sqrts: tf.Tensor) -> tf.Tensor:
    dtype = sqrts.dtype
    complex_factor = tf.complex(
        tf.constant([1, 0, -1, 0], dtype=dtype), tf.constant([0, 1, 0, -1], dtype=dtype)
    )
    sqrt_pi = tf.cast(tf.sqrt(tf.constant(np.pi, dtype)), complex_factor.dtype)
    one = tf.cast(1, complex_factor.dtype)
    return (
        sqrt_pi
        * tf.where(labels[2] % 2 == 0, one, -one)
        * tf.gather(complex_factor, (tf.math.reduce_sum(labels[1:], axis=0) % 4))
        * tf.gather(tf.cast(sqrts, dtype=complex_factor.dtype), 2 * labels[0] + 1)
    )


def single_spin_factor(labels: tf.Tensor, sqrts: tf.Tensor, spin: int = 0) -> tf.Tensor:
    dtype = sqrts.dtype
    complex_factor = tf.complex(
        tf.constant([1, 0, -1, 0], dtype=dtype), tf.constant([0, 1, 0, -1], dtype=dtype)
    )
    spin_factor = complex_factor[spin % 4] * complex_factor[(2 * spin) % 4]
    sqrt_pi = tf.cast(tf.sqrt(tf.constant(np.pi, dtype)), complex_factor.dtype)
    return (
        sqrt_pi
        * spin_factor
        * tf.gather(complex_factor, labels[1] % 4)
        * tf.gather(tf.cast(sqrts, dtype=complex_factor.dtype), 2 * labels[0] + 1)
    )


def gmm_factor(
    hsampling: Union[HarmonicSampling, tf.Tensor, int],
    sqrts: Optional[tf.Tensor] = None,
    dtype: Union[str, np.dtype, tf.DType] = tf.float32,
) -> tf.Tensor:
    from tensossht.sampling import harmonic_sampling_scheme

    if not isinstance(hsampling, HarmonicSampling):
        hsampling = harmonic_sampling_scheme(hsampling)
    dtype = tf.as_dtype(dtype)
    if sqrts is None:
        sqrts = tf.sqrt(tf.cast(tf.range(2 * (hsampling.lmax + 1) + 1), dtype=dtype))
    elif sqrts.dtype != dtype:
        sqrts = tf.cast(sqrts, dtype)
    if hsampling.smin == hsampling.smax:
        return single_spin_factor(hsampling.labels, sqrts, spin=hsampling.smin)
    result = many_spins_factor(hsampling.labels, sqrts)
    if hsampling.is_separable_spin:
        return tf.reshape(result, (hsampling.nspins, -1))
    return result


def gmm_to_coeffs(
    hsampling: Union[HarmonicSampling, tf.Tensor, int],
    dtype: Union[str, np.dtype, tf.DType] = tf.float32,
) -> GmmToCoeffs:
    from tensossht.sampling import harmonic_sampling_scheme

    if not isinstance(hsampling, HarmonicSampling):
        hsampling = harmonic_sampling_scheme(hsampling)
    dtype = tf.dtypes.as_dtype(dtype)

    sqrts = tf.sqrt(tf.cast(tf.range(2 * (hsampling.lmax + 1) + 1), dtype=dtype))
    factor = gmm_factor(hsampling, sqrts, dtype=dtype)
    deltadelta_iterator = DeltaDeltaIterator.factory(hsampling, dtype=dtype)
    return GmmToCoeffs(hsampling, factor, deltadelta_iterator, dtype=dtype)
