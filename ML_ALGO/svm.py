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
        
        # K is a matrix which stores dot product of all vectors 
        # K[1,1] is dot product of m1 vector with itself
        # k[:,1] is dot product of m1 vector with all other vectors        
        self.K = None
        
        # It is the list of alphas which comes zero for non support vector
        self.alpha = None
        
    def fit(self,x,y=None):
        
        self._setup_input(x,y)
        
        self.K = np.zeros((self.n_samples,self.n_samples))
        
        # calculating the vector multiplication(dot) of all vectors
        
        for i in range(self.n_samples):
            self.K[:,i] = self.kernel(self.x,self.x[i,:])        
            
        self.alpha = np.zeros(self.n_samples)
        self.sv_idx = np.arange(0,self.n_samples)
        
        self._train()
    
    
        