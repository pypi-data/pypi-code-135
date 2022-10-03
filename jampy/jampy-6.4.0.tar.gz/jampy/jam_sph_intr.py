"""
##############################################################################

Copyright (C) 2022, Michele Cappellari
E-mail: michele.cappellari_at_physics.ox.ac.uk

Updated versions of the software are available from my web page
http://purl.org/cappellari/software

If you have found this software useful for your research,
I would appreciate an acknowledgement to the use of the
"JAM modelling method of Cappellari (2008)"

This software is provided as is without any warranty whatsoever.
Permission to use, for non-commercial purposes is granted.
Permission to modify for personal or internal use is granted,
provided this copyright and disclaimer are included unchanged
at the beginning of the file. All other rights are reserved.
In particular, redistribution of the code is not allowed.

##############################################################################

MODIFICATION HISTORY:
    V1.0.0: Written and tested.
       Michele Cappellari, Oxford, 3 October 2022

"""

from scipy import special
import numpy as np

from jampy.quad1d import quad1d

##############################################################################

def integrand(t, sigma_lum, sigma_pot, lum, mass, Mbh, rmin, beta, component):
    """
    Implements the integrand of equation (40) of Cappellari (2008, MNRAS).

    """ 
    # TANH Change of variables for Jeans r-integral (Sec.6.2 of Cappellari 2020, MNRAS, 494, 4819)
    # np.log([1e-6*np.median(sigma), 3*np.max(sigma)]) -> [r, inf]
    drdt = np.exp(t)
    r = rmin + drdt[:, None]    # Broadcast over radii and MGE parameters

    G = 0.004301  # (km/s)^2 pc/Msun [6.674e-11 SI units (CODATA2018)]
    h = r/(np.sqrt(2)*sigma_pot)
    mass_r = Mbh + (mass*(special.erf(h) - 2/np.sqrt(np.pi)*h*np.exp(-h**2))).sum(1)  # eq.(49) of Cappellari (2008)

    func = (r/rmin)**(2*beta)/r**2                                                    # eq.(40) of Cappellari (2020)
    fnu = func*lum*np.exp(-0.5*(r/sigma_lum)**2)/(np.sqrt(2*np.pi)*sigma_lum)**3      # eq.(47) of Cappellari (2008)

    if component == 'sig2r':
        fnu = fnu.sum(1)
    elif component == 'sig2th':
        fnu = (fnu*(1 - beta)).sum(1)

    integ = G*fnu*mass_r   # Vector of values computed at different radii

    return integ*drdt

##############################################################################

class jam_sph_intr:

    """
    PURPOSE
    -------

    This procedure calculates a prediction for the intrinsic second moment
    <v_r^2> in the radial direction for a spherically symmetric MGE model.
    It implements the solution of the anisotropic Jeans equations
    presented in equation (40) of `Cappellari (2008, MNRAS, 390, 71).
    <https://ui.adsabs.harvard.edu/abs/2008MNRAS.390...71C>`_

    CALLING SEQUENCE
    ----------------

    .. code-block:: python

        from jampy.jam_sph_intr import jam_sph_intr

        jam = jam_sph_intr(dens_lum, sigma_lum, dens_pot, sigma_pot, mbh, rad, beta=None)
        sigma_r = np.sqrt(jam.model)

    INPUT PARAMETERS
    ----------------

    dens_lum:
        vector of length N containing the peak surface brightness of the
        MGE Gaussians describing the galaxy surface brightness in units of
        Lsun/pc^2 (solar luminosities per parsec^2).
    SIGMA_LUM:
        vector of length N containing the dispersion in pc of
        the MGE Gaussians describing the galaxy surface brightness.
    SURF_POT:
        vector of length M containing the peak value of the MGE Gaussians
        describing the galaxy surface density in units of Msun/pc^2 (solar
        masses per parsec^2). This is the MGE model from which the model
        potential is computed.

    SIGMA_POT:
        vector of length M containing the dispersion in pc of
        the MGE Gaussians describing the galaxy surface density.
    MBH:
        Mass of a nuclear supermassive black hole in solar masses.
    RAD:
        Vector of length P with the (positive) radius from the galaxy center
        in pc at which one wants to compute the model predictions.

    Optional Keywords
    -----------------

    BETA:
        Vector of length N with the anisotropy
        beta = 1 - (sigma_theta/sigma_r)^2 of the individual MGE Gaussians.
        A scalar can be used if the model has constant anisotropy.

    Output Parameters
    -----------------

    Returned as attributes of the ``jam_sph_intr`` class.

    .flux: array_like  with shape (p,)
        Vector with the MGE luminosity density at each ``(R, z)`` location in
        ``Lsun/pc^3``, used to plot the isophotes on the model results.
    .model: array_like with shape (2, p)
        Contains ``[sig2r, sig2th]`` defined as follows:

        sig2r: array_like with shape (p,)
            squared intrinsic dispersion in ``(km/s)^2`` along the r
            direction at each ``r`` location.

        sig2th: array_like with shape (p,)
            squared intrinsic dispersion in ``(km/s)^2`` along the th
            direction at each ``r`` location.

    """

    def __init__(self, dens_lum, sigma_lum, dens_pot, sigma_pot, mbh, rad, beta=None):

        if beta is None:
            beta = np.zeros_like(dens_lum)
        assert len(dens_lum) == len(sigma_lum) == len(beta), 'dens_lum, sigma_lum and beta must have the same length'
        assert len(dens_pot) == len(sigma_pot), 'surf_pot and sigma_pot must have the same length'

        lum = dens_lum*(np.sqrt(2*np.pi)*sigma_lum)**3
        mass = dens_pot*(np.sqrt(2*np.pi)*sigma_pot)**3

        sig2r, sig2th, nu = np.empty((3, rad.size))
        lim = np.log([1e-6*np.median(sigma_lum), 3*np.max(sigma_lum)])
        nu = (dens_lum*np.exp(-0.5*(rad[:, None]/sigma_lum)**2)).sum(1)
        for j, rj in enumerate(rad):
            args = [sigma_lum, sigma_pot, lum, mass, mbh, rj, beta]
            sig2r[j], sig2th[j] = \
                [quad1d(integrand, lim, epsabs=0, singular=0, args=args+[txt]).integ/nu[j]
                 for txt in ['sig2r', 'sig2th']]

        self.flux = nu
        self.rad = rad
        self.model = sig2r, sig2th

##############################################################################
