from typing import Any, Callable, Optional, Tuple, Union, cast

import numpy as np
import tensorflow as tf

from tensossht.iterators import DeltaDeltaIterator, LIterator
from tensossht.references import REFERENCES
from tensossht.sampling import HarmonicAxes, HarmonicSampling, ImageSamplingSchemes
from tensossht.typing import TFArray


class CoeffsToFmm:
    f"""Computes Fmm from coefficients.

    See [McEwen, Wiaux (20011)], equation 14. Also includes normalization for real
    signals, modulation for image-space sampling, and padding for missing harmonic
    coefficients (e.g. mmin != -lmax + 1).

    This functor creates as small a matrix as `mmin` and `mmax` allow. It also avoids
    creating :math:`m < 0` since those can be obtained by symmetry.

    {REFERENCES['MW']}
    """

    def __init__(
        self,
        summation: Callable[[TFArray], TFArray],
        modulator: Callable[[TFArray], TFArray],
        padding: Callable[[TFArray], TFArray],
    ):
        self.summation = summation
        self.modulator = modulator
        self.padding = padding

    def __call__(
        self, coefficients: TFArray, axes: Optional[HarmonicAxes] = None
    ) -> TFArray:
        from tensossht.sampling import Axis

        if axes is not None:
            coefficients = axes.transpose(coefficients, Axis.SPIN, Axis.COEFF)
        coeff_sum = self.summation(coefficients)
        perm = list(range(1, len(coeff_sum.shape) - 1)) + [0, len(coeff_sum.shape) - 1]
        modulated = self.modulator(tf.transpose(coeff_sum, perm=perm))
        return self.padding(modulated)


def coeffs_to_fmm(
    hsampling: Optional[Union[int, TFArray, HarmonicSampling]],
    sampling: Union[str, ImageSamplingSchemes] = ImageSamplingSchemes.MW,
    dtype: Union[np.dtype, tf.DType, str] = tf.float32,
) -> CoeffsToFmm:
    from functools import partial

    from tensossht.sampling import harmonic_sampling_scheme, image_sampling_scheme

    rdtype = tf.dtypes.as_dtype(dtype).real_dtype
    sampling = image_sampling_scheme(sampling)
    hsampling = harmonic_sampling_scheme(hsampling)
    if hsampling.is_multi_spin and not hsampling.is_separable_spin:
        msg = "Summation without a separate spin dimension has not been implemented"
        raise NotImplementedError(msg)
    if sampling == ImageSamplingSchemes.MWSS and hsampling.is_complex:
        sampling_size = 2 * hsampling.lmax
        modulator = noop
        padding = complex_mwss_padding
    elif sampling == ImageSamplingSchemes.MWSS:
        sampling_size = 2 * hsampling.lmax
        modulator = noop
        padding = real_mwss_padding
    elif hsampling.is_complex:
        sampling_size = 2 * hsampling.lmax - 1
        modulator = partial(tf.math.multiply, mw_modulation(hsampling.lmax, rdtype))
        padding = complex_mw_padding
    else:
        sampling_size = 2 * hsampling.lmax - 1
        modulator = partial(tf.math.multiply, mw_modulation(hsampling.lmax, rdtype))
        padding = real_mw_padding

    summation = cast(
        Callable[[TFArray], TFArray],
        CoeffToFmmSummation.factory(hsampling, sampling_size, rdtype),
    )
    return CoeffsToFmm(
        summation=summation,
        modulator=modulator,
        padding=partial(
            padding,
            lmax=hsampling.lmax,
            lmin=hsampling.lmin,
            mmax=hsampling.mmax,
            mmin=hsampling.mmin,
        ),
    )


class CoeffToFmmSummation:
    f"""Sums coefficients into :math:`_sF_{{mm'}}` matrix.

    See [McEwen, Wiaux (20011)], equation 14.

    This functor creates as small a matrix as `mmin` and `mmax` allow. It also avoids
    creating :math:`m < 0` since those can be obtained by symmetry.

    {REFERENCES['MW']}
    """

    def __init__(
        self,
        hsampling: Union[TFArray, HarmonicSampling, int],
        sampling_size: Optional[int] = None,
        factor: Optional[TFArray] = None,
        deltadelta_iterator: Optional[DeltaDeltaIterator] = None,
        scale_factor: Optional[TFArray] = None,
        sqrts: Optional[TFArray] = None,
        dtype: Union[str, np.dtype, tf.DType] = tf.float32,
    ):
        from functools import partial

        from tensossht.iterators import sign_condition
        from tensossht.sampling import harmonic_sampling_scheme
        from tensossht.specialfunctions import legendre_lsum

        if not isinstance(hsampling, HarmonicSampling):
            hsampling = harmonic_sampling_scheme(hsampling)

        self.hsampling = hsampling
        rdtype = tf.dtypes.as_dtype(dtype).real_dtype
        self.lmax = hsampling.lmax

        if sqrts is None:
            sqrts = tf.math.sqrt(
                tf.cast(tf.range(2 * (hsampling.lmax + 1) + 1), dtype=rdtype)
            )
        assert sqrts is not None
        if deltadelta_iterator is None:
            deltadelta_iterator = DeltaDeltaIterator.factory(
                hsampling, dtype=rdtype, sqrts=sqrts
            )
        self.deltadelta_iterator = deltadelta_iterator

        if scale_factor is None:
            scale_factor = summation_scale_factor(
                hsampling, sqrts, sampling_size, rdtype
            )
        self.scale_factor = scale_factor
        self.sign_condition = sign_condition(hsampling)

        self._lsum = partial(
            legendre_lsum,
            lmax=hsampling.lmax,
            lmin=hsampling.lmin,
            mmax=hsampling.mmax,
            mmin=hsampling.mmin,
            axis=-1,
        )

        if factor is None:
            factor = spin_factor(hsampling, rdtype)
        self.factor = factor

    @tf.function
    def __call__(self, coefficients: TFArray) -> TFArray:
        """Sums coefficients into :math:`_sF_{{mm'}}` matrix.

        args:
            coefficients: an array with shape `(*batch, spins, coeffs)`
        returns:
            An array with shape `(m', *batch, spins, m)` where `m` and `m'` are the
            max order of the harmonics.
        """
        assert coefficients.dtype in {tf.complex64, tf.complex128}
        self.deltadelta_iterator.reset()

        state = self.deltadelta_iterator.tf_state
        # Axis manipulations to simplify gather and summation itself.
        result = tf.TensorArray(coefficients.dtype, size=2 * self.lmax - 1)
        for mp in tf.range(self.lmax - 1, -1, -1):
            deltadelta, state = cast(
                Tuple[TFArray, Any], self.deltadelta_iterator.next(state)
            )
            deltas = tf.cast(deltadelta * self.scale_factor, dtype=coefficients.dtype)
            summand = cast(TFArray, coefficients * deltas)
            result = result.write(mp, self._lsum(summand))

            if mp != 0:  # -mp branch
                summee = self._lsum(tf.where(self.sign_condition, summand, -summand))
                result = result.write(2 * self.lmax - 1 - mp, summee)

        return result.stack() * self.factor

    @classmethod
    def factory(
        cls,
        hsampling: Optional[Union[int, TFArray, HarmonicSampling]],
        sampling_size: Optional[int] = None,
        dtype: Union[str, np.dtype, tf.DType] = tf.float32,
    ):
        from tensossht.sampling import harmonic_sampling_scheme

        hsampling = harmonic_sampling_scheme(hsampling)
        if hsampling.is_multi_spin and not hsampling.is_separable_spin:
            msg = "Summation without a separate spin dimension has not been implemented"
            raise NotImplementedError(msg)
        rdtype = tf.dtypes.as_dtype(dtype).real_dtype
        sqrts = tf.sqrt(tf.cast(tf.range(2 * (hsampling.lmax + 1) + 1), dtype=rdtype))
        deltadelta_iterator = DeltaDeltaIterator.factory(
            hsampling, sqrts=sqrts, dtype=rdtype
        )

        return cls(
            hsampling,
            deltadelta_iterator=deltadelta_iterator,
            sampling_size=sampling_size,
            sqrts=sqrts,
            dtype=dtype,
        )


class CoeffToFmmLSummation:
    f"""Sums coefficients into :math:`_sF_{{mm'}}` matrix.

    See [McEwen, Wiaux (20011)], equation 14.

    The summation occurs over the degree :math:`l`.

    {REFERENCES['MW']}
    """

    def __init__(
        self,
        hsampling: Union[TFArray, HarmonicSampling, int],
        sampling_size: Optional[int] = None,
        dtype: Union[str, np.dtype, tf.DType] = tf.float32,
    ):
        from tensossht.sampling import harmonic_sampling_scheme

        if not isinstance(hsampling, HarmonicSampling):
            hsampling = harmonic_sampling_scheme(hsampling)

        assert hsampling.is_separable_spin
        assert hsampling.mmin == -hsampling.mmax
        assert hsampling.mmax == hsampling.lmax - 1

        self.hsampling = hsampling
        rdtype = tf.dtypes.as_dtype(dtype).real_dtype
        cdtype = tf.complex(
            tf.constant(0, dtype=rdtype), tf.constant(0, dtype=rdtype)
        ).dtype
        self.lmax = hsampling.lmax

        sampling_size = sampling_size or (2 * hsampling.lmax - 1)
        sfactor = tf.constant(
            np.array([1, -1j, -1, 1j])[
                np.arange(hsampling.smin, hsampling.smax + 1) % 4
            ],
            dtype=cdtype,
        )
        mfactor = tf.constant(
            np.array([1, -1j, -1, 1j])[
                np.arange(hsampling.mmin, hsampling.mmax + 1) % 4
            ],
            dtype=cdtype,
        )
        mpfactor: TFArray = tf.cast(  # type: ignore
            1 - 2 * (tf.range(hsampling.mmin, hsampling.mmax + 1) % 2), dtype=cdtype
        )
        self.factor = (
            tf.cast(
                tf.constant(sampling_size * sampling_size, dtype=rdtype)
                / tf.sqrt(tf.constant(4 * np.pi, dtype=rdtype)),
                dtype=mfactor.dtype,
            )
            * mfactor[:, None, None, None]
            * sfactor[None, None, :, None]
            * mpfactor[None, None, None, :]
        )

    def output_shape(self, batch_size: int = 1):
        msize = tf.reduce_max(self.hsampling[1]) - tf.reduce_min(self.hsampling[1])
        ssize = tf.reduce_max(self.hsampling[2]) - tf.reduce_min(self.hsampling[2])
        return tf.TensorShape([batch_size, msize, msize, ssize])

    def __call__(self, coefficients: TFArray) -> TFArray:
        """Sums coefficients into :math:`_sF_{{mm'}}` matrix.

        args:
            coefficients: an array with shape `(*batch, coeffs)` for spinless
            coefficients or `(*batch, spins, coeffs)` for multi-spin coefficients.
        returns:
            An array with shape `(m', *batch, m)` or `(m', *batch, spins, m)` where `m`
            and `m'` are the max order of the harmonics.
        """
        from functools import reduce
        from operator import mul

        assert coefficients.dtype in {tf.complex64, tf.complex128}

        def make_delta_ls(order: int, delta: TFArray) -> TFArray:
            smin, smax = self.hsampling.smin, self.hsampling.smax
            dls = CoeffToFmmLSummation.delta_ls(delta, order, smin, smax)
            return tf.transpose(dls)

        if self.hsampling.nspins == 1:
            reshape = reduce(mul, coefficients.shape[:-1], 1), 1, coefficients.shape[-1]
        else:
            reshape = (
                reduce(mul, coefficients.shape[:-2], 1),
                coefficients.shape[-2],
                coefficients.shape[-1],
            )
        spin_coeffs = tf.reshape(coefficients, reshape)

        lmin = min(abs(u) for u in range(self.hsampling.smin, self.hsampling.smax + 1))

        inputs = tf.RaggedTensor.from_row_lengths(
            tf.transpose(spin_coeffs, tf.roll(tf.range(spin_coeffs.ndim), 1, 0)),
            2 * tf.range(lmin, self.hsampling.lmax) + 1,
        )

        iterator = LIterator(max_degree=self.hsampling.lmax, dtype=coefficients.dtype)
        for _ in range(0, lmin):
            next(iterator)
        delta_l = LIterator.symmetrize(lmin, next(iterator))
        # inputs -> (l, m, b, s)
        # delta_l -> (m, m')
        # delta_ls -> (s, m')
        # result -> (m, b, s, m')
        result = (
            inputs[0][:, :, :, None]  # type: ignore
            * delta_l[:, None, None, :]
            * make_delta_ls(lmin, delta_l)[None, None, :, :]
        )
        for degree, delta_coeffs in enumerate(iterator, start=lmin + 1):
            delta_l = LIterator.symmetrize(degree, delta_coeffs)
            result = tf.pad(result, [[1, 1], [0, 0], [0, 0], [1, 1]]) + (
                inputs[degree - lmin][:, :, :, None]  # type: ignore
                * delta_l[:, None, None, :]
                * make_delta_ls(degree, delta_l)[None, None, :, :]
                * tf.sqrt(tf.constant(2 * degree + 1, delta_l.dtype))
            )

        number_of_m = self.hsampling.mmax - self.hsampling.mmin + 1
        out_shape = number_of_m, *coefficients.shape[:-1], number_of_m
        return tf.reshape(
            tf.signal.ifftshift(
                tf.transpose(result * self.factor, [3, 1, 2, 0]), axes=0
            ),
            out_shape,
        )

    @staticmethod
    def delta_ls(delta_l: TFArray, order: int, smin: int, smax: int) -> TFArray:
        assert smin <= smax
        dls = delta_l[:, order - min(order, smax) : order - max(-order, smin) + 1]
        dls = dls[:, ::-1]
        if order >= abs(smin) and order >= abs(smax):
            return dls
        return tf.pad(
            dls, [[0, 0], [max(-order, smin) - smin, smax - min(order, smax)]]
        )

    @classmethod
    def factory(
        cls,
        hsampling: Optional[Union[int, TFArray, HarmonicSampling]],
        dtype: Union[str, np.dtype, tf.DType] = tf.float32,
    ):
        from tensossht.sampling import harmonic_sampling_scheme

        hsampling = harmonic_sampling_scheme(hsampling)
        if hsampling.is_multi_spin and not hsampling.is_separable_spin:
            msg = "Summation without a separate spin dimension has not been implemented"
            raise NotImplementedError(msg)

        return cls(hsampling, dtype=dtype)


def mw_modulation(lmax: int, dtype: Union[np.dtype, tf.DType, str] = tf.float32):
    from tensossht.transforms.images_to_fmm import mw_modulation

    modulation = mw_modulation(lmax, dtype)
    return tf.expand_dims(tf.signal.ifftshift(tf.math.conj(modulation)), axis=-1)


def real_mw_padding(
    unsymmetrized: TFArray, lmax: int, lmin: int, mmax: int, mmin: int
) -> TFArray:
    """Pad Fmpm for mmin and lmin."""
    return _mw_padding(unsymmetrized, lpad=mmin, rpad=lmax - 1 - mmax)


def complex_mw_padding(
    unsymmetrized: TFArray, lmax: int, lmin: int, mmax: int, mmin: int
) -> TFArray:
    """Pad Fmpm for mmin and lmin."""
    return _mw_padding(unsymmetrized, lpad=mmin + lmax - 1, rpad=lmax - 1 - mmax)


def real_mwss_padding(
    unsymmetrized: TFArray, lmax: int, lmin: int, mmax: int, mmin: int
) -> TFArray:
    """Pad Fmpm for mmin and lmin."""
    return _mwss_padding(unsymmetrized, lmax, lpad=mmin, rpad=lmax - 1 - mmax)


def complex_mwss_padding(
    unsymmetrized: TFArray, lmax: int, lmin: int, mmax: int, mmin: int
) -> TFArray:
    """Pad Fmpm for mmin and lmin."""
    return _mwss_padding(unsymmetrized, lmax, lpad=mmin + lmax, rpad=lmax - 1 - mmax)


def _mw_padding(unsymmetrized: TFArray, lpad: int, rpad: int) -> TFArray:
    """Pad Fmpm for mmin and lmin."""
    ndim = tf.rank(unsymmetrized)
    padding = tf.concat((tf.zeros((ndim - 1, 2), dtype=tf.int32), [[lpad, rpad]]), 0)
    return tf.pad(unsymmetrized, padding)


def _mwss_padding(unsymmetrized: TFArray, lmax: int, lpad: int, rpad: int):
    """Pad Fmpm for mmin and lmin."""
    # add mp column
    ndim = tf.rank(unsymmetrized)
    mpcol = tf.concat(
        (
            unsymmetrized[..., :lmax, :],
            tf.zeros(tf.shape(unsymmetrized[..., 0:1, :]), dtype=unsymmetrized.dtype),
            unsymmetrized[..., lmax:, :],
        ),
        ndim - 2,
    )
    # fill matrix with missing mmin and missing MWSS column
    padding = tf.concat((tf.zeros((ndim - 1, 2), dtype=tf.int32), [[lpad, rpad]]), 0)
    return tf.pad(mpcol, padding)


def noop(x):
    return x


def spin_factor(
    hsampling: HarmonicSampling, dtype: Union[np.dtype, tf.DType, str] = tf.float32
) -> TFArray:
    if hsampling.is_multi_spin and hsampling.is_separable_spin:
        return many_spin_factor(hsampling, dtype)
    return single_spin_factor(hsampling, dtype)


def single_spin_factor(
    hsampling: HarmonicSampling, dtype: Union[np.dtype, tf.DType, str] = tf.float32
) -> TFArray:
    rdtype = tf.dtypes.as_dtype(dtype).real_dtype
    cdtype = tf.complex(tf.constant(0, rdtype), tf.constant(0, rdtype)).dtype
    jfac = tf.constant([(1 / 1j) ** i for i in range(4)], dtype=cdtype)
    indices = (
        tf.range(
            max(hsampling.mmin, 1 - hsampling.lmax),
            min(hsampling.mmax + 1, hsampling.lmax),
        )
        + hsampling.smin
    )
    return tf.gather(jfac, indices % 4) * jfac[(2 * hsampling.smin) % 4]


def many_spin_factor(
    hsampling: HarmonicSampling, dtype: Union[np.dtype, tf.DType, str] = tf.float32
) -> TFArray:
    rdtype = tf.dtypes.as_dtype(dtype).real_dtype
    cdtype = tf.complex(tf.constant(0, rdtype), tf.constant(0, rdtype)).dtype
    mfactor = tf.constant([(1 / 1j) ** i for i in range(4)], dtype=cdtype)
    mindices = tf.range(
        max(hsampling.mmin, 1 - hsampling.lmax), min(hsampling.mmax + 1, hsampling.lmax)
    )
    sfactor = tf.constant([(-1 / 1j) ** i for i in range(4)], dtype=cdtype)
    return (
        tf.gather(mfactor, mindices % 4)[None]
        * tf.gather(sfactor, hsampling.spins % 4)[:, None]
    )


def summation_scale_factor(
    hsampling: HarmonicSampling,
    sqrts: TFArray,
    sampling_size: Optional[int] = None,
    dtype: Union[np.dtype, tf.DType, str] = tf.float32,
) -> TFArray:
    sampling_size = sampling_size or (2 * hsampling.lmax - 1)
    rdtype = tf.dtypes.as_dtype(dtype).real_dtype
    if hsampling.is_multi_spin and hsampling.is_separable_spin:
        llabels = tf.reshape(hsampling.llabels, (hsampling.nspins, -1))[0]
    else:
        llabels = hsampling.llabels
    return tf.gather(sqrts, 2 * llabels + 1) * (
        tf.cast(sampling_size**2, dtype=rdtype)
        / tf.sqrt(tf.constant(4 * np.pi, dtype=rdtype))
    )
