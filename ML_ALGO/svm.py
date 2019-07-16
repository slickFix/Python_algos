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
        # k[:,4] is dot product of m4 vector with all other vectors  
        # k[i,j] is dot product of mi vector with mj vector
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
    
    # Utility functions
    
    def random_index(self,i):
        ''' Used for calculation of random index for alpha '''
        z = i 
        while z==i:
            z = np.random.randint(0,self.n_samples)        
        return z
        
    def _find_bounds(self,i,j):
        
        """
        Find L and H such that L <= alpha <= H.
        Also, alpha must satisfy the constraint 0 <= αlpha <= C.        
        """
        
        if self.y[i] != self.y[j]:
            L = max(0,self.alpha[j]-self.alpha[i])
            H = min(self.C,self.C - self.alpha[i] + self.alpha[j])
        else:
            L = max(0,self.alpha[i] + self.alpha[j] - self.C)
            H = min(self.C,self.alpha[i] +  self.alpha[j])
            
        return L,H
    
    def _clip(self,alpha,L,H):
        
        if alpha > H:
            alpha = H
        
        if alpha < L:
            alpha = L
        
        return alpha
        