# this file is to store the utils functions for the project

from quspin.operators import hamiltonian
import contextlib
import numpy as np


####################################
# OI utils functions
####################################

def hamiltonian_s(*args, **kwargs):
    # silence mode of the `hamiltonian` function (otherwise the output is too verbose)
    with contextlib.redirect_stdout(None):
        return hamiltonian(*args, **kwargs)


####################################
# numeric utils functions
####################################

def normalize(x, normal_val=1, norm_type='sum'):
    if norm_type == 'sum':
        return x / np.sum(x) * normal_val
    else:
        raise NotImplementedError("Only `sum` norm is implemented.")
    
