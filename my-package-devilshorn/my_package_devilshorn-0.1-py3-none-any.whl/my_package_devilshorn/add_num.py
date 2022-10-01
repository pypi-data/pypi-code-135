import numpy as np

def get_sum(num=None,*numbers):
    sum = 0
    if not num:
        num = [i for i in numbers]
    for i in num:
        sum+=i
    return sum

def np_sum(num=None,*numbers):
    if not num:
        num = [i for i in numbers]
    return np.sum([i for i in num])

# nums = [int(i) for i in input('enter the  numbers').split(' ')]
# print(get_sum(1,2,3,4,5))
# print(np_sum(1,2,3,4,5))