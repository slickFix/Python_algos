#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 22:58:36 2019

@author: siddharth
"""

import numpy as np
import scipy.spatial.distance  as dist


''' Defining vararious types of kernels for svm '''

class Linear:
    
    def __call__(self,x,y):
        return np.dot(x,y.T)
    
    def __repr__(self):
        return 'Linear Kernel'

class Poly:
    
    def __init__(self,degree = 2):
        self.degree = 2
        
    def __call__(self,x,y):
        
        return np.dot(x,y.T)** self.degree
    
    def __rept__(self):
        
        return 'Polynomial Kernel'
    
class RBF:
    
    def __init__(self,gamma = 0.1):
        self.gamma = gamma
        
    def __call__(self,x,y):
        x = np.atleast_2d(x)
        y = np.atleast_2d(y)
        
        return np.exp(-self.gamma * dist.cdist(x,y) ** 2).flatten()
    
    def __repr__(self):
        
        return 'RBF kernel'