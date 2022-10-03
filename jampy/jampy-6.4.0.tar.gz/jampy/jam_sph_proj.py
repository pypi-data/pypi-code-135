"""
##############################################################################

Copyright (C) 2004-2022, Michele Cappellari
E-mail: michele.cappellari_at_physics.ox.ac.uk

Updated versions of the software are available from my web page
http://purl.org/cappellari/software

If you have found this software useful for your research,
I would appreciate an acknowledgement to the use of the
"JAM modelling method of Cappellari (2008, 2020)"

This software is provided as is without any warranty whatsoever.
Permission to use, for non-commercial purposes is granted.
Permission to modify for personal or internal use is granted,
provided this copyright and disclaimer are included unchanged
at the beginning of the file. All other rights are reserved.
In particular, redistribution of the code is not allowed.

##############################################################################

MODIFICATION HISTORY:
    V1.0.0: Written and tested isotropic case.
       Michele Cappellari, Vicenza, 10 August 2004
    V2.0.0: Included anisotropic case with 1D integral. MC, Oxford, 4 April 2008
    V3.1.0: First released version. MC, Oxford, 12 August 2008
    V3.2.0: Updated documentation. MC, Oxford, 14 August 2008
    V4.0.0: Implemented PSF convolution using interpolation on polar grid.
        Dramatic speed-up of calculation. Further documentation.
        MC, Oxford, 11 September 2008
    V4.0.1: Included keyword STEP. MC, Windhoek, 29 September 2008
    V4.0.2: Added keywords NRAD. Thanks to Michael Williams for reporting possible
        problems with too coarse interpolation. MC, Oxford, 21 November 2008
    V4.1: Added keywords CHI2, ERMS, ML, /PRINT, /QUIET, RMS as in the
        JAM_AXISYMMETRIC_RMS routine. Updated the usage example routine
        TEST_JAM_SPHERICAL_RMS. MC, Oxford, 04 February 2010
    V4.1.1: Correct missing value at R=0 in plot. MC, Oxford, 29 September 2011
    V4.1.2: Use renamed CAP_* routines to avoid potential naming conflicts.
       MC, Paranal, 8 November 2013
    V5.0.0: Translated from IDL into Python. MC, Oxford, 3 April 2014
    V5.0.1: Support both Python 2.6/2.7 and Python 3.x. MC, Oxford, 25 May 2014
    V5.0.2: Updated documentation. MC, Oxford, 5 August 2014
    V5.1.0: Included proper motion calculations using the keyword "tensor".
      - Fully broadcast integrand. MC, Oxford, 22 April 2015
    V5.1.1: Removed dependency on special.hyp2f1. MC, Oxford, 28 April 2015
    V5.1.2: Use odd kernel size for convolution.
      - Fixed corner case with coordinates falling outside the
        interpolation region, due to finite machine precision.
        MC, Oxford, 17 February 2017
    V5.1.3: Updated documentation. Fixed DeprecationWarning in Numpy 1.12.
        MC, Oxford, 17 March 2017
    V5.1.4: Make default `step` depend on `sigmapsf` regardless of `pixsize`.
        MC, Oxford, 10 September 2017
    V5.1.5: Print a message when no PSF convolution was performed.
      - Broadcast kernel loop. MC, Oxford, 22 January 2018
    V5.1.6: Check that PSF is normalized. MC, Oxford, 7 March 2018
    V5.1.7: Changed imports for JamPy as a package.
      - Removed example. MC, Oxford, 17 April 2018
    V5.1.8: Dropped Python 2.7 support. MC, Oxford, 12 May 2018
    V5.1.9: Fixed clock DeprecationWarning in Python 3.7.
        MC, Oxford, 27 September 2018
    V5.1.10: Use analytic MGE in convolution. MC, Oxford, 31 October 2019
    V5.1.11: Included special isotropic case, for accuracy tests.
        Used TANH change of variable before quadrature with quad1d(singular=0).
        Use simplified integrand formulas from Cappellari (2020).
        Use recurrence relations instead of repeated calls of beta and gamma.
        MC, Oxford, 7 February 2022
    V5.1.12: Included Osipkov-Merritt anisotropy for testing.
        MC, Oxford, 5 September 2022
    V5.1.13: Make quadrature limits insensitive to scaling.
        MC, Oxford, 3 October 2022

"""

from scipy import special, ndimage, signal
import numpy as np
from time import perf_counter as clock
import matplotlib.pyplot as plt

from jampy.quad1d import quad1d

##############################################################################

def bilinear_interpolate(xv, yv, im, xout, yout):
    """
    The input array has size im[ny, nx] as in the output
    of im = f(meshgrid(xv, yv))
    xv and yv are vectors of size nx and ny respectively.
    map_coordinates is equivalent to IDL's INTERPOLATE.

    """
    ny, nx = np.shape(im)
    assert (nx, ny) == (xv.size, yv.size), "Input arrays dimensions do not match"

    xi = (nx-1.)/(xv[-1] - xv[0]) * (xout - xv[0])
    yi = (ny-1.)/(yv[-1] - yv[0]) * (yout - yv[0])

    return ndimage.map_coordinates(im.T, [xi, yi], order=1, mode='nearest')

##############################################################################

def ibetam(a, b, x):
    """
    Incomplete beta function defined as the Mathematica Beta[x, a, b]:
    Beta[x, a, b] = Integral[t^(a - 1) * (1 - t)^(b - 1), {t, 0, x}]
    This routine only works for (0 < x < 1) & (b > 0) as required by JAM.

    """
    # V1.0: Michele Cappellari, Oxford, 01/APR/2008
    # V2.0: Use Hypergeometric function for negative a or b.
    #    Eq.(8.17.7) of Olver et al. (2010) https://dlmf.nist.gov/8.17.E7
    #    MC, Oxford, 04/APR/2008
    # V3.0: Use recurrence relation for (a < 0) & (b > 0)
    #    Eq.(8.17.20) of Olver et al. (2010) https://dlmf.nist.gov/8.17.E20
    #    After suggestion by Gary Mamon. MC, Oxford, 16/APR/2009

    a = a + 4.76123e-7  # Perturb to avoid singularities in gamma and betainc
    if np.all(a > 0):
        ib = special.betainc(a, b, x)
    else:
        p = int(np.ceil(abs(np.min(a))))
        tot = 0
        gam1 = special.gamma(a + b)
        gam2 = special.gamma(1 + a)
        for j in range(p):
            tot += gam1/gam2*x**(j + a)
            gam1 *= j + b + a   # Gamma recurrence https://dlmf.nist.gov/5.5#E1
            gam2 *= j + 1 + a
        ib = tot*(1 - x)**b/special.gamma(b) + special.betainc(a + p, b, x)

    return ib*special.beta(a, b)

##############################################################################

def _integrand(t, sig_l, sig_m, lum, mass, Mbh, rmin, beta, tensor, ra):
    """
    This function implements the integrand of equation (50) of Cappellari (2008, hereafter C08).
    Also implemented are the expressions for the proper motion components (pmr, pmt) from 
    Appendix B3 of Cappellari (2020, https://ui.adsabs.harvard.edu/abs/2020MNRAS.494.4819C)

    """ 
    # TANH Change of variables for Jeans r-integral
    # np.log([1e-6, 3*np.max(sigma_lum)]) -> [R, inf]
    drdt = np.exp(t)
    r = rmin + drdt[:, None]    # Broadcast over radii and MGE parameters

    if ra is not None:  # Osipkov-Merritt anisotropy: eq.A12 of Mamon & Lokas (2005, MNRAS)

        func = (2*ra**2 + rmin**2)/(ra**2 + rmin**2)**1.5 \
               * (r**2 + ra**2)/r**2 * np.arctan(np.sqrt((r**2 - rmin**2)/(ra**2 + rmin**2))) \
               - rmin**2/(ra**2 + rmin**2)*np.sqrt(r**2 - rmin**2)/r**2

    elif np.all(beta == 0):           # Simpler formula for isotropic case

        func = 2*np.sqrt(r**2 - rmin**2)/r**2

    else:

        if np.all(beta == beta[0]):
            beta = beta[0]          # faster calculation when beta is a scalar

        w = (rmin/r)**2
        bwp = ibetam(beta + 0.5, 0.5, w)
        bwm = (beta*bwp + np.sqrt(1 - w)*w**(beta - 0.5))/(beta - 0.5)  # = ibetam(beta - 0.5, 0.5, w) https://dlmf.nist.gov/8.17#E20
        gam = special.gamma(beta - 0.5)
        gap = gam*(beta - 0.5)              # = special.gamma(beta + 0.5) https://dlmf.nist.gov/5.5#E1
        pg = np.sqrt(np.pi)/special.gamma(beta)

        k = w**(1 - beta)/rmin
        a = pg*gam - bwm                    # eq.(B11a) of Cappellari (2020)
        b = pg*gap - beta*bwp               # eq.(B11b) of Cappellari (2020)

        if tensor == 'los':
            func = k*(a - b)                # eq.(B10a) of Cappellari (2020)
        elif tensor == 'pmr':
            func = k*((1 - beta)*a + b)     # eq.(B10b) of Cappellari (2020)
        elif tensor == 'pmt':
            func = k*(1 - beta)*a           # eq.(B10c) of Cappellari (2020)

    fnu = (func*lum*np.exp(-0.5*(r/sig_l)**2)/(np.sqrt(2*np.pi)*sig_l)**3).sum(1)     # eq.(B4) of Cappellari (2020)
    G = 0.004301  # (km/s)^2 pc/Msun [6.674e-11 SI units (CODATA2018)]
    h = r/(np.sqrt(2)*sig_m)
    mass_r = Mbh + (mass*(special.erf(h) - 2/np.sqrt(np.pi)*h*np.exp(-h**2))).sum(1)    # eq.(B6) of Cappellari (2020)

    integ = G*fnu*mass_r   # Vector of values computed at different radii

    return integ*drdt

##############################################################################

def second_moment(R, sig_l, sig_m, lum, mass, Mbh, beta, tensor, ra,
                     sigmaPsf, normPsf, step, nrad, surf_l, pixSize):
    """
    This routine gives the second V moment after convolution with a PSF.
    The convolution is done using interpolation of the model on a
    polar grid, as described in Appendix A of Cappellari (2008).

    """
    psfConvolution = (np.max(sigmaPsf) > 0) and (pixSize > 0)
    lim = np.log([1e-6*np.median(sig_l), 3*np.max(sig_l)])

    if psfConvolution: # PSF convolution

        # Kernel step is 1/4 of largest value between sigma(min) and 1/2 pixel side.
        # Kernel half size is the sum of 3*sigma(max) and 1/2 pixel diagonal.
        #
        if step == 0:
            step = np.min(sigmaPsf)/4.
        mx = 3*np.max(sigmaPsf) + pixSize/np.sqrt(2)

        # Make grid linear in log of radius RR
        #
        rmax = np.max(R) + mx # Radius of circle containing all data + convolution
        logRad = np.linspace(np.log(step/np.sqrt(2)), np.log(rmax), nrad)   # Linear grid in np.log(rr)
        rr = np.exp(logRad)

        # The model Vrms computation is only performed on the radial grid
        # which is then used to interpolate the values at any other location
        #
        wm2Pol = np.empty_like(rr)
        for j, rj in enumerate(rr):     # Integration of equation (50)
            args = (sig_l, sig_m, lum, mass, Mbh, rj, beta, tensor, ra)
            wm2Pol[j] = quad1d(_integrand, lim, epsabs=0, singular=0, args=args).integ

        nx = int(np.ceil(rmax/step))
        x1 = np.linspace(0.5 - nx, nx - 0.5, 2*nx)*step
        xCar, yCar = np.meshgrid(x1, x1)  # Cartesian grid for convolution

        # Interpolate MGE model and Vrms over cartesian grid.
        # Division by mgePol before interpolation reduces interpolation error
        r = np.sqrt(xCar**2 + yCar**2)
        mgeCar = (surf_l*np.exp(-0.5*(r[..., None]/sig_l)**2)).sum(-1)
        mgePol = (surf_l*np.exp(-0.5*(rr[:, None]/sig_l)**2)).sum(-1)
        wm2Car = mgeCar*np.interp(np.log(r), logRad, wm2Pol/mgePol)

        nk = int(np.ceil(mx/step))
        kgrid = np.linspace(-nk, nk, 2*nk + 1)*step
        xgrid, ygrid = np.meshgrid(kgrid, kgrid) # Kernel is square

        # Compute kernel with equation (A6) of Cappellari (2008).
        # Normaliztion is irrelevant here as it cancels out.
        #
        dx = pixSize/2
        sp = np.sqrt(2)*sigmaPsf
        xg, yg = xgrid[..., None], ygrid[..., None]
        kernel = normPsf*(special.erf((dx - xg)/sp) + special.erf((dx + xg)/sp)) \
                        *(special.erf((dx - yg)/sp) + special.erf((dx + yg)/sp))
        kernel = np.sum(kernel, 2)   # Sum over PSF components

        # Seeing and aperture convolution with equation (A3)
        #
        muCar = np.sqrt(signal.fftconvolve(wm2Car, kernel, mode='same')
                      / signal.fftconvolve(mgeCar, kernel, mode='same'))

        # Interpolate convolved image at observed apertures.
        # Aperture integration was already included in the kernel.
        #
        sigp = bilinear_interpolate(x1, x1, muCar, R/np.sqrt(2), R/np.sqrt(2))

    else: # No PSF convolution: just compute values

        sigp = np.empty_like(R)
        for j, rj in enumerate(R):
            args = (sig_l, sig_m, lum, mass, Mbh, rj, beta, tensor, ra)
            wm2Pol = quad1d(_integrand, lim, epsabs=0, singular=0, args=args).integ
            mgePol = np.sum(surf_l*np.exp(-0.5*(rj/sig_l)**2))
            sigp[j] = np.sqrt(wm2Pol/mgePol)

    return sigp, psfConvolution

##############################################################################

class jam_sph_proj:

    """
    PURPOSE
    -------

    This procedure calculates a prediction for any of the three components of the
    the projected second velocity moments V_RMS = sqrt(V^2 + sigma^2), or for a
    non-rotating galaxy V_RMS = sigma, for an anisotropic spherical galaxy model.
    It implements the solution of the anisotropic Jeans equations
    presented in equation (50) of `Cappellari (2008, MNRAS, 390, 71).
    <https://ui.adsabs.harvard.edu/abs/2008MNRAS.390...71C>`_
    PSF convolution is done as described in the Appendix of Cappellari (2008).
    This procedure includes the proper motions calculation given in
    Appendix B3 of `Cappellari (2020, MNRAS, 494, 4819)
    <https://ui.adsabs.harvard.edu/abs/2020MNRAS.494.4819C>`_

    CALLING SEQUENCE
    ----------------

    .. code-block:: python

        from jampy.jam_sph_proj import jam_sph_proj

        jam = jam_sph_proj(surf_lum, sigma_lum, surf_pot, sigma_pot, mbh,
            distance, rad, beta=None, errors=None, ml=None, normpsf=1, nrad=50,
            pixsize=0, plot=True, quiet=False, data=None, sigmapsf=0, step=0,
            tensor='los', scale=None)
        sigma_los_model = jam.model

    INPUT PARAMETERS
    ----------------

    SURF_LUM:
        vector of length N containing the peak surface brightness of the
        MGE Gaussians describing the galaxy surface brightness in units of
        Lsun/pc^2 (solar luminosities per parsec^2).
    SIGMA_LUM:
        vector of length N containing the dispersion in arcseconds of
        the MGE Gaussians describing the galaxy surface brightness.
    SURF_POT:
        vector of length M containing the peak value of the MGE Gaussians
        describing the galaxy surface density in units of Msun/pc^2 (solar
        masses per parsec^2). This is the MGE model from which the model
        potential is computed.

        In a common usage scenario, with a self-consistent model, one has
        the same Gaussians for both the surface brightness and the potential.
        This implies SURF_POT = SURF_LUM, SIGMA_POT = SIGMA_LUM.
        The M/L, by which SURF_POT has to be multiplied to best match the
        data, is fitted by the routine when passing the RMS and ERMS
        keywords with the observed kinematics.

    SIGMA_POT:
        vector of length M containing the dispersion in arcseconds of
        the MGE Gaussians describing the galaxy surface density.
    MBH:
        Mass of a nuclear supermassive black hole in solar masses.

        VERY IMPORTANT: The model predictions are computed assuming SURF_POT
        gives the total mass. In the common self-consistent case one has
        SURF_POT = SURF_LUM and if requested (keyword ML) the program can scale
        the output RMSMODEL to best fit the data. The scaling is equivalent to
        multiplying *both* SURF_POT and MBH by a factor M/L. To avoid mistakes,
        the actual MBH used by the output model is printed on the screen.
    DISTANCE:
        distance of the galaxy in Mpc.
    RAD:
        Vector of length P with the (positive) radius from the galaxy center
        in arcseconds of the bins (or pixels) at which one wants to compute
        the model predictions.

        When no PSF/pixel convolution is performed (SIGMAPSF=0 or PIXSIZE=0)
        there is a singularity at RAD=0 which should be avoided.

    OPTIONAL KEYWORDS
    -----------------

    BETA:
        Vector of length N with the anisotropy
        beta = 1 - (sigma_theta/sigma_R)^2 of the individual MGE Gaussians.
        A scalar can be used if the model has constant anisotropy.
    errors:
        Vector of length P with the 1sigma errors associated to the RMS
        measurements. From the error propagation
        ERMS = sqrt((dVel*velBin)^2 + (dSig*sigBin)^2)/RMS,
        where velBin and sigBin are the velocity and dispersion in each bin
        and dVel and dSig are the corresponding errors
        (Default: constant errors ERMS=0.05*MEDIAN(RMS)).
    ML:
        Mass-to-light ratio to multiply the values given by SURF_POT.
        Setting this keyword is completely equivalent to multiplying the
        output RMSMODEL by SQRT(M/L) after the fit. This implies that the
        BH mass becomes MBH*(M/L).

        If this keyword is set to a negative number in input, the M/L is
        fitted from the data and the keyword returns the best-fitting M/L
        in output. The BH mass of the best-fitting model is MBH*(M/L).
    NORMPSF:
        Vector of length Q with the fraction of the total PSF flux
        contained in the various circular Gaussians describing the PSF of the
        observations. It has to be total(NORMPSF) = 1. The PSF will be used for
        seeing convolution of the model kinematics.
    NRAD:
        Number of logarithmically spaced radial positions for which the
        models is evaluated before interpolation and PSF convolution. One may
        want to increase this value if the model has to be evaluated over many
        orders of magnitutes in radius (default: NRAD=50).
    PIXSIZE:
        Size in arcseconds of the (square) spatial elements at which the
        kinematics is obtained. This may correspond to the size of the spaxel
        or lenslets of an integral-field spectrograph. This size is used to
        compute the kernel for the seeing and aperture convolution.

        If this is not set, or PIXSIZE = 0, then convolution is not performed.
    PLOT:
        Set this keyword to produce a plot at the end of the calculation.
    QUIET:
        Set this keyword not to print values on the screen.
    data:
        Vector of length P with the input observed stellar
        V_RMS=sqrt(velBin^2 + sigBin^2) at the coordinates positions
        given by the vector RAD.

        If RMS is set and ML is negative or not set, then the model is fitted to
        the data, otherwise the adopted ML is used and just the chi^2 is returned.
    SIGMAPSF:
        Vector of length Q with the dispersion in arcseconds of the
        circular Gaussians describing the PSF of the observations.

        If this is not set, or SIGMAPSF = 0, then convolution is not performed.

        IMPORTANT: PSF convolution is done by creating a 2D image, with pixels
        size given by STEP=MAX(SIGMAPSF,PIXSIZE/2)/4, and convolving it with
        the PSF + aperture. If the input radii RAD are very large with respect
        to STEP, the 2D image may require a too large amount of memory. If this
        is the case one may compute the model predictions at small radii
        separately from those at large radii, where PSF convolution is not
        needed.
    STEP:
        Spatial step for the model calculation and PSF convolution in arcsec.
        This value is automatically computed by default as
        STEP=MAX(SIGMAPSF,PIXSIZE/2)/4. It is assumed that when PIXSIZE or
        SIGMAPSF are big, high resolution calculations are not needed. In some
        cases however, e.g. to accurately estimate the central Vrms in a very
        cuspy galaxy inside a large aperture, one may want to override the
        default value to force smaller spatial pixels using this keyword.

        Use this keyword to set the desired scale of the model when no PSF or
        pixel convolution is performed (SIGMAPSF=0 or PIXSIZE=0).
    TENSOR:
        Specifies any of the three component of the projected velocity dispersion
        tensor one wants to calculate. Possible options are (i) "los" (default) for
        the line-of-sight component; (ii) "pmr" for tha radial component of the proper
        motion second moment and (iii) "pmt" for the tangential component of the proper
        motion second moment. All three components are computed in km/s at the adopted
        distance.

    OUTPUT PARAMETERS
    -----------------

    attributes of the ``jam_sph_proj`` class

    model:
        Vector of length P with the model predictions for the velocity
        second moments (sigma in the spherical non-rotating case) of each bin.
        The line-of-sigh component or either of the proper motion components can
        be obtained in output using the ``tensor`` keyword.
    ml:
        best fitting M/L.
    chi2:
        Reduced chi^2 describing the quality of the fit::

            chi^2 = total( ((rms-rmsModel)/erms)^2 ) / n_elements(rms)
    """

    def __init__(self, surf_lum, sigma_lum, surf_pot, sigma_pot, mbh, distance,
                 rad, beta=None, errors=None, ml=None, normpsf=1, nrad=50,
                 pixsize=0, plot=True, quiet=False, data=None, sigmapsf=0,
                 step=0, tensor='los', scale=None):

        if beta is None:
            beta = np.zeros_like(surf_lum)
        assert len(surf_lum) == len(sigma_lum) == len(beta), 'surf_lum, sigma_lum and beta must have the same length'
        assert len(surf_pot) == len(sigma_pot), 'surf_pot and sigma_pot must have the same length'
        assert tensor in ["los", "pmr", "pmt"], 'tensor must be: los, pmr or pmt'
        if scale is not None:
            assert tensor == 'los', "Only tensor='los' implemented for Osipkov-Merritt"
        if (errors is None) and (data is not None):
            errors = np.full_like(data, np.median(data)*0.05)  # Constant ~5% errors

        sigmapsf = np.atleast_1d(sigmapsf)
        normpsf = np.atleast_1d(normpsf)
        assert sigmapsf.size == normpsf.size, "sigmaPSF and normPSF do not match"
        assert round(np.sum(normpsf), 2) == 1, "PSF not normalized"

        pc = distance*np.pi/0.648 # Constant factor to convert arcsec --> pc

        sigmaPsf = sigmapsf*pc
        pixsize_pc = pixsize*pc
        step_pc = step*pc

        if scale is not None:
            scale = scale*pc

        sigma_lum_pc = sigma_lum*pc     # Convert from arcsec to pc
        lum = 2*np.pi*surf_lum*sigma_lum_pc**2

        sigma_pot_pc = sigma_pot*pc     # Convert from arcsec to pc
        mass = 2*np.pi*surf_pot*sigma_pot_pc**2

        t = clock()
        model, psfConvolution = second_moment(rad*pc, sigma_lum_pc,
            sigma_pot_pc, lum, mass, mbh, beta, tensor, scale, sigmaPsf,
            normpsf, step_pc, nrad, surf_lum, pixsize_pc)

        if not quiet:
            print('jam_sph_rms elapsed time sec: %.2f' % (clock() - t))
            if not psfConvolution:
                txt = "No PSF convolution:"
                if np.max(sigmapsf) == 0:
                    txt += " sigmapsf == 0;"
                if pixsize == 0:
                    txt += " pixsize == 0;"
                print(txt)

        self.pixsize = pixsize
        self.rad = rad
        self.data = data
        self.errors = errors
        self.model = model

        ####### Output and optional M/L fit
        # If `data`` keyword is not given all this section is skipped

        if data is not None:

            if (ml is None) or (ml <= 0):

                # eq. (51) of Cappellari (2008, MNRAS)
                d, m = data/errors, model/errors
                scale = (d @ m)/(m @ m)
                ml = scale**2

            else:
                scale = np.sqrt(ml)

            model *= scale
            chi2 = np.sum(((data - model)/errors)**2)/data.size

            if not quiet:
                print(f'beta[0]={beta[0]:.2f}; M/L={ml:#.3g}; '
                      f'BH={mbh*ml:#.3g}; chi2/DOF={chi2:#.3g}')
                print(f'Total mass MGE: {np.sum(mass*ml):#.4g}')

            if plot:
                self.plot()
        else:

            ml = None
            chi2 = None

        self.ml = ml
        self.chi2 = chi2

##############################################################################

    def plot(self):

        rad1 = self.rad.clip(0.38*self.pixsize)
        plt.clf()
        plt.errorbar(rad1, self.data, yerr=self.errors, fmt='o')
        plt.plot(rad1, self.model, 'r')
        plt.xscale('log')
        plt.xlabel('R (arcsec)')
        plt.ylabel(r'$\sigma$ (km/s)')

##############################################################################
