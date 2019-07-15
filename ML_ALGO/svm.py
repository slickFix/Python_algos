#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 09:54:39 2019

@author: siddharth
"""

from base_estimator import BaseEstimator
from kernels import Linear

import numpy as np

np.random.seed(2019)

'''
SVM optimization using SMO(sequential minimal optimization) algorithm

reference:- http://cs229.stanford.edu/materials/smo.pdf

'''

class SVM(BaseEstimator):
    
    def __init__(self,C=1.0,tol=1e-3,kernel = None,max_iter = 100):
        
        ''' Support vector machine implementation using simplified SMO 
        
        parameters
        --------------
        
        C: float,default 1.0 [penalty]
        tol: float,default 1e-3 [tolerance]
        kernel: Kernel object
        max_iter: int, default 100 [maximum iteration]
        
        '''
        
        self.C = C
        self.tol = tol
        self.max_iter = max_iter
        
        if kernel is None:
            self.kernel = Linear()
        
        else:
            self.kernel = kernel
            
        self.b = 0
        self.K = None
        self.alpha = None
            
        