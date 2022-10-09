import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import math as m

def func_2_fit(n):
  return np.array(list(map(m.log2, n)))
  return n**3
  
def fit_func_2_times(timings: np.ndarray, func_2_fit: callable):
	if len(timings.shape) == 1:
		timings = timings.reshape(-1, 1)
	values = func_2_fit(timings[ :, 0]).reshape(-1, 1)
	#normalizar timings
	times = timings[ : , 1] / timings[0, 1]
	#ajustar a los valores en times un modelo lineal sobre los valores en values
	lr_m = LinearRegression()
	lr_m.fit(values, times)
	return lr_m.predict(values)
  
def matrix_multiplication(m_1: np.ndarray, m_2: np.ndarray)-> np.ndarray:
  n_rows,n_interm,n_columns= m_1.shape[0],m_2.shape[0],m_2.shape[1]

  m_product=np.zeros((n_rows,n_columns))
  
  for p in range(n_rows):
    for q in range(n_columns):
      for r in range(n_interm):
        m_product[p,q] += m_1[p,r] * m_2[r,q]

  return m_product

def bb(t: list, f: int, l: int, key: int)-> int:

  while f<=l:
    if f == l:                                          
      if key == t[f]:
        return f
      else:
        return None
    mid = (f + l) // 2
    if key == t[mid]:                                   
      return mid
    if t[mid] < key:                                    
      f = mid                   
    elif t[mid] > key:                                 
      l = mid

  return None
    
def rec_bb(t: list, f: int, l: int, key: int)-> int:  #Definición de la cabecera de la función

	if l >= f:
		  mid = (l + f) // 2
		  if t[mid] == key:
		     return mid
		  elif t[mid] > key:
		     return rec_bb(t, f, mid - 1, key)
		  else:
		     return rec_bb(t, mid + 1, l, key)
	else:
		  return -1  
		  
def min_heapify(h: np.ndarray, i: int):
    while 2*i+1 < len(h):
      n_i = i
      if h[n_i] > h[2*i+1]:
        n_i = 2*i+1
      if 2*i+2 < len(h) and h[n_i] > h[2*i+2]:
        n_i = 2*i+2
      if n_i > i:
        h[i], h[n_i] = h[n_i], h[i]
        i = n_i
      else:
        return
        
def insert_min_heap(h: np.ndarray, k: int)-> np.ndarray:

  h = np.append(h, k)

  j = len(h) -1

  while j >=1 and h[(j-1) // 2] > h[j]:
    h[(j-1) // 2], h[j] = h[j], h[(j-1) // 2]
    j = (j-1) // 2

  return h
  
def create_min_heap(h: np.ndarray):
  while j > -1:
    min_heapify(h, j)
    j -= 1
  return h
  
def pq_ini():
  return np.array([])

def pq_insert(h: np.ndarray, k: int)-> np.ndarray:
  h = np.append(h, k)
  return h;
  
def pq_remove(h: np.ndarray) -> np.ndarray:
  max_val = 0
  for i in range(len(h)):
      if h[i] < h[max_val]:
          max_val = i
  item = h[max_val]
  h = np.delete(h, max_val)
  return h, item
  
def select_min_heap(h: np.ndarray, k: int)-> int:
  h = [-i for i in h]
  l = h[k:]
  h = h[:k]
  h = create_min_heap(h)
  for i in l:
    if h[0] < i:
      h[0] = i
      min_heapify(h,0)
  return -h[0]
