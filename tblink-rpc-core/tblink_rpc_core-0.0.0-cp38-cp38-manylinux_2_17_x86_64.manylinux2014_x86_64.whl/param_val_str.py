'''
Created on Jul 5, 2021

@author: mballance
'''

class ParamValStr(object):
    
    def __init__(self, val):
        self._val = val
        
    def val(self):
        return self._val
        
    def accept(self, v):
        v.visit_str(self)