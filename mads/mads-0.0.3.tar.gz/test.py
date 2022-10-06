import numpy as np
from mads import mads

def objective_function(d):
    f = (d[0] - 0.3)**2 + (d[1] + 0.2)**2
    
    return f


design_variables = np.array([0, 0])
bounds_lower = np.array([-1, -1])
bounds_upper = np.array([1, 1])
dp_tol = 1E-6
nitermax = 1000

mads.mads(design_variables, bounds_upper, bounds_lower, objective_function, dp_tol, nitermax, True)