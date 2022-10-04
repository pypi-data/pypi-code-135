# %%
import numpy as np
import pandas as pd
import math
from math import *
import os

# %%
a = 6378137 #semimajor axis
f = 1/298.25722356 #flattening factor
b = a*(1-f) #semiminor axis
e1 = sqrt((a**2-b**2) / a**2) #first eccentricity
e2 = sqrt((a**2-b**2) / b**2)  #second eccentricity

# %%
#Util trig functions
sind = lambda x : np.sin(np.deg2rad(x))
cosd = lambda x : np.cos(np.deg2rad(x))
atand = lambda x : np.rad2deg(np.arctan(x))

# %%
#Principal curvature
def N(phi):
    return a / sqrt(1 - e1**2 * sind(phi)**2)

# %%
def lla2xyz(phi, lam, h):
    """
        lla2xyz(phi,lamb,h)

    Takes coordinates in LLA format (latitude=phi, longitude=lamb, altitude=h) to ECEF format (X,Y,Z).
    Latitudes and longitudes are taken as positive degree values being North and East respectively. 
    """
    X = (N(phi) + h) * cosd(phi) * cosd(lam)
    Y = (N(phi) + h) * cosd(phi) * sind(lam)
    Z = (b**2/a**2 * N(phi) + h) * sind(phi)

    return np.array([X,Y,Z])

# %%
def xyz2phih(X, Y, Z):
    p = sqrt(X**2 + Y**2)
    h = 0
    phi = atand(Z / (p * (1 - e1**2)))

    for i in range(round(N(phi) * 1e-3)):
        h = p / cosd(phi) - N(phi)
        phi = atand(Z / (p * (1-e1**2 * N(phi) / (N(phi) + h))))
    
    return phi,h

# %%
def xyz2lla(X, Y, Z):
    """
        xyz2lla(X,Y,Z)

    Takes coordinates in ECEF format (`X`,`Y`,`Z`) to LLA format (latitude=`phi`, longitude=`lamb`, altitude=`h`).
    """

    phi,h = xyz2phih(X,Y,Z)
    lam = atand(Y/X)

    return np.array([phi,lam,h])

# %%

def triangle(x, a=-1, m=0, b=1):
    """
    A triangle "bump" function for use as a basis function in `lin_interp`. 
    `a` and `b` are the x intercepts values of the triangle. 
    `m` is the point where it reaches its highest value of `1`
    """
    if x > a and x <= m:
        return 1/(m-a)*(x-a)
    elif x > m and x < b:
        return 1/(b-m)*(b-x)
    else:
        return 0.

# %%
def lin_interp(t, xs, ys):
    """
        lin_interp(t, xs, ys)

    Returns the value of the linear interpolation of `ys` at value `t` in `xs`. `xs` and `ys` should be equal length arrays.
    Uses triangular basis functions over `xs` scaled by the corresponding values in `ys` to generate an interpolating function for
    some value `t`.

    Example
    xs = [1,2,3,4]
    ys = [6,7,8,9]

    #arguments to `a`,`m`,`b` in `triangle` in parentheses
    [0 1 2 3 4 0] = padded `xs` array
    (0 1 2) * ys[1] +
    (1 2 3) * ys[2] +
        (2 3 4) * ys[3] +
        (3 4 0) * ys[4]
    """
    #constructs a padded array from `xs`
    pxs = np.hstack((0,xs,0))
    #Performs a convolution over `xs` of `ys` and the `triangle` basis functions. 
    return np.dot(ys, [triangle(t,pxs[i], pxs[i+1], pxs[i+2]) for i in range(len(xs))])

# %%
#Data transformations
#Import data
def time_series_analysis(): 
    df = pd.read_csv(os.path.dirname(__file__) + "/lla_coordinate_time_series.csv",names=["T","phi", "lamb","h"])
    #converts altitude to meters
    df['h'] = df['h'] * 1000

    #converts latitude, longitude, altitude to XYZ position vectors 
    df['P'] = df[['phi', 'lamb','h']].apply(lambda x : lla2xyz(x['phi'], x['lamb'], x['h']), axis=1)

    #breaks XYZ positions into X, Y, Z vectors for easier plotting 

    df[['X','Y','Z']] = [*df['P']]
    #computes differences in adjacents times for velocity calculation
    df['dT'] = df['T'].diff()
    df['dT'] = df['dT'].fillna(1)

    #computes differences in adjacents positions for velocity calculation
    df['dP'] = df['P'].diff()
    df['dP'] = [np.zeros(3) if x is np.NaN else x for x in df['dP'] ]

    #divides position difference by time differences to obtain velocity
    df['V'] = df[['dP','dT']].apply(lambda x : x['dP'] / x['dT'],  axis=1)

    #breaks V velocities into X, Y, Z vectors for easier plotting
    df[['Vx','Vy','Vz']] = [*df['V']]

    # %%
    #print to stdout for two time values. 
    t1,t2 = 1532334000, 1532335268
    v1,v2 = lin_interp(t1, df['T'],df['V']), lin_interp(t2, df['T'],df['V'])
    print("Velocity at Unix time ", t1, ":\n",v1,"m/s")
    print("Velocity at Unix time ", t2, ":\n",v2,"m/s")
