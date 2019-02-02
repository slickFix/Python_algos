#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 21:13:52 2019

@author: siddharth
"""



import os
os.chdir('/home/siddharth/workspace-python/Python/Building TensorFlow API from Scratch/')
path  = os.getcwd()


import sys
sys.path.append(path)

from operation import *


class BinaryOperation(Operation):
    def __init__(self,a,b):
        super().__init__([a,b])
        

class Add(BinaryOperation):
    """ add element wise , a+b """
    
    def forward(self,a,b):
        return a+b
    
    def backward(self,a,b):
        pass
    

class Multiply(BinaryOperation):
    """ multiply element wise, a*b """
    
    def forward(self,a,b):
        return a*b
    
    def backward(self,a,b):
        pass
    
    
class Divide(BinaryOperation):
    """ divide element wise, a/b """
    
    def forward(self,a,b):
        import numpy as np
        return np.true_divide(a,b)
    
    def backward(self,a,b):
        pass
    
class MatMul(BinaryOperation):
    """ muiltiply two matrices a and b , a*b """
    
    def forward(self,a,b):
        
        import numpy as np
        
        return np.dot(a,b)
    
    def backward(self,a,b):
        pass