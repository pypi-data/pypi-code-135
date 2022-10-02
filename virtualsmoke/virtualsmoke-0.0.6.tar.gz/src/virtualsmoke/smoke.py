#!/usr/bin/env python3
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import joblib
import numpy as np
from pkg_resources import resource_filename
import fire, math


class Smoke:
  reg_model_path = resource_filename(__name__, 'mfp_model.h5') 
  model_scaler_path = resource_filename(__name__, 'meanpathcaler.gz') 
  constants = {
    "thr": 0.5624121779859484, # classification threshold
    "a": 29.195, # coefficient a
    "b": 2.63165e-10, # coefficient b
    "c": 2.57e-8, # coefficient c
    "k": 1.38064852e-23, # boltzman constant
    "m": 0.02897 # molecular mass of Air
  }



  def __init__(self,*args):
  	pass


  @classmethod  
  def loadmodel(cls):
    loaded_model = joblib.load(open(f'{cls.reg_model_path}', 'rb'))
    return loaded_model


  @classmethod
  def getMfp(cls, T):
    a = cls.constants.get('a')
    b = cls.constants.get('b')
    c = cls.constants.get('c')
    m = cls.constants.get('m')
    k = cls.constants.get('k')
    return (a * math.sqrt(math.pi * k * T/(2*m)) + b*T - c) * 10e8


  @classmethod  
  def prepareInput(cls,T,H,P):
    M = cls.getMfp(T)
    testdata = np.array([[M,H,P]])
    scaler = joblib.load(f'{cls.model_scaler_path}')
    return scaler.transform(testdata)


  @classmethod
  def SignalGenerator(cls,T,H,P):
    scalledInput = cls.prepareInput(T,H,P)
    thr = cls.constants.get('thr')
    return (cls.loadmodel().predict_proba(scalledInput)[:,1] > thr).astype(int)[0]





def signal(T, H,P):
  try:
    return Smoke.SignalGenerator(T,H,P)
  except Exception as e:
    print(e)


if __name__ == '__main__':
  fire.Fire(signal)
