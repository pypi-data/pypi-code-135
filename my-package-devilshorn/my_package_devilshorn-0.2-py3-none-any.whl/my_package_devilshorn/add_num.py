import numpy as np

def get_sum(*numbers):
    sum = 0
    for i in [i for i in numbers]:
        sum+=i
    return sum

def np_sum(num=None,*numbers):
    return np.sum([i for i in numbers])