
from scipy.interpolate import griddata
import astropy.units as u
import numba
import pandas as pd
import numpy as np
import os
import sys

from .relations import  scale_to_local_lf, teff_to_spt_kirkpatrick, \
spt_to_teff_kirkpatrick, teff_to_spt_pecaut, spt_to_teff_pecaut
from .core_tools import sample_from_powerlaw

#DATA_FOLDER=os.environ['POPSIMS_DATA_FOLDER']

#CODE_FOLDER=os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))
#sys.path.append(CODE_FOLDER)
#DATA_FOLDER= CODE_FOLDER+'/data/'

def _read_bintemplates():
    from .binaries import BINARIES 
    #must be a pickle file with columns prim, sec, sys all floats
    tbl=pd.DataFrame(BINARIES)
    return [tbl.prim.values, tbl.sec.values, tbl.sys.values]


def get_system_type(pr, sc):
    """
    1D- Random draw by using numpy search on a grid
    Args:
    ----
        x_grid: grid of values ( array)
        cdf:  corresponding values from the CDF
        nsample: optional, number of samples
    Returns:
    -------
        random draws

    Examples:
    --------
        > x = np.arange(0, 10)
        > cdf = x**3/(x[-1]**3)
        > res= random_draw(x, cdf)
    """
    interpolators= _read_bintemplates()
    #where secondary are nans set to primaries
    sc[np.isnan(sc)]=pr[np.isnan(sc)]
    #interpolate
    interpoints=np.array([interpolators[0], interpolators[1] ]).T
    comb=griddata(interpoints, interpolators[-1] , (pr, sc), method='linear')
    #rember to assign <15 =primary and > 39= primary
    return comb


def evolutionary_model_interpolator( mass, age, model, subset=None):
    """
    1D- Random draw by using numpy search on a grid
    Args:
    ----
        x_grid: grid of values ( array)
        cdf:  corresponding values from the CDF
        nsample: optional, number of samples
    Returns:
    -------
        random draws

    Examples:
    --------
        > x = np.arange(0, 10)
        > cdf = x**3/(x[-1]**3)
        > res= random_draw(x, cdf)

    """
    from .evol_models import EVOL_MODELS
    evolutiomodel=pd.DataFrame(EVOL_MODELS[model])

    #use the full cloud treatment for saumon models
    if subset != None:
         evolutiomodel=(evolutiomodel[evolutiomodel[subset[0]]==subset[1]]).reset_index(drop=True)
 
    #make age, teff, mass logarithm scale
    valuest=np.log10(evolutiomodel.temperature.values)
    #valueslogg=evolutiomodel.gravity.values
    valueslumn=evolutiomodel.luminosity.values

    valuesm=np.log10(evolutiomodel.mass.values)
    valuesag=np.log10(evolutiomodel.age.values)

    evolpoints=np.array([valuesm, valuesag ]).T

    teffs=griddata(evolpoints, valuest , (np.log10(mass), np.log10(age)), method='linear')
    lumn=griddata(evolpoints, valueslumn , (np.log10(mass), np.log10(age)), method='linear')

    return {'mass': mass*u.Msun, 'age': age*u.Gyr, 'temperature': 10**teffs*u.Kelvin, 
    'luminosity': lumn*u.Lsun}