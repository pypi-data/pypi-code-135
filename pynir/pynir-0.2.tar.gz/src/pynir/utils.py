# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:02:36 2022

@author: Jin Zhang (zhangjin@mail.nankai.edu.cn)
"""
import numpy as np
from scipy.stats import norm

def simulateNIR(nSample = 100, nComp = 3, refType = 1, noise = 0.0, seeds = 1):
    """
    simulating NIR spectra

    Parameters
    ----------
    nSample : int, optional
        number of samples. The default is 100.
    
    nComp : int, optional
        number of componnet for spectral simulation. The default is 3.
    
    refType : int, optional
        type of reference value
        None for no reference value output
        1 for contious values as reference value output
        2 or the larger integer for binary or class output.
        
    seeds : int, optimal
        random seed for generating spectra and reference values. The default is 1.

    Returns
    -------
    X:  matrix, simulated NIR spectra matrix.
    y: array, concentration or class of all samples.

    """
    wv = np.linspace(1000,2500,500) #wavelength
    np.random.seed(seeds)
    conc = np.random.random((nSample,nComp))
    mu = np.random.random(nComp)*1500+1000
    sigma = np.random.random(nComp)*100+100
    spcBase = [norm.pdf(wv, mu[i],sigma[i]) for i in range(nComp)]
    X = np.dot(conc,spcBase)
    X = X + np.random.randn(*X.shape)*noise
    conc = conc + np.random.randn(*conc.shape)*noise
    if refType == 0:
        y = None
    elif refType == 1:
        y = conc[:,1]
    elif refType > 1:
        y = np.zeros((conc[:,1].shape),dtype=int)
        yquantile = np.linspace(0,1,refType+1)
        for i in range(refType):
            if i == refType-1:
                conditioni = np.logical_and(conc[:,1] >= np.quantile(conc[:,1],yquantile[i]), conc[:,1] <= np.quantile(conc[:,1],yquantile[i+1]))
            else:
                conditioni = np.logical_and(conc[:,1] >= np.quantile(conc[:,1],yquantile[i]), conc[:,1] < np.quantile(conc[:,1],yquantile[i+1]))
            y = y + conditioni*i
    else:
        raise ValueError("refType only allow integer larger than 0 as input")
                
    return X, y, wv


def classificationEvaluation():
    pass

    
def regressionEvalutaion():
    pass