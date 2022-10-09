__all__ = ["REFERENCES"]

from textwrap import dedent

REFERENCES = {
    "MW": dedent(
        """
        .. [McEwen, Wiaux (2011)]
            Jason D. McEwen, Yves Wiaux
            A novel sampling theorem on the sphere.
            IEEE Transactions on Signal Processing 59 (12), 5876 - 5887 (2011).
            https://doi.org/10.1109/TSP.2011.2166394
        """
    ),
    "TN": dedent(
        """
        .. [Trapani, Navaza (2006)]
            Trapani, S., Navaza, J.
            Calculation of spherical harmonics and Wigner d functions by FFT.
            Applications to fast rotational matching in molecular replacement and
            implementation into AMoRe
            Acta Crystallographica Section A (2006). A62, 262-269
            https://doi.org/10.1107/S0108767306017478
        """
    ),
    "KR": dedent(
        """
        .. [Kostelec, Rockmore (2008)]
            Kostelec, P.J., Rockmore, D.N.
            FFTs on the Rotation Group.
            J Fourier Anal Appl 14, 145–179 (2008).
            https://doi.org/10.1007/s00041-008-9013-5
        """
    ),
}
