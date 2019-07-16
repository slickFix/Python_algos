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
        
            
    def _train(self):
        
        iters = 0 
        
        while iters < self.max_iter:
            iters+=1
            
            alpha_prev = np.copy(self.alpha)
            
            for j in range(self.n_samples):
                
                # Picking random i
                i = self.random_index(j)
                
                eta = 2.0 * self.K[i,j] - self.K[i,i] - self.K[j,j]
                
                if eta >= 0:
                    continue
                
                L,H = self._find_bounds(i,j)
                
                # Error for current examples
                e_i,e_j =self._error(i),self._error(j)
                
                # save old alphas
                alpha_io, alpha_jo = self.alpha[i] , self.alpha[j]
                
                # update alpha
                self.alpha[j] -= (self.y[j]* (e_i-e_j))/eta
                self.alpha[j] = self._clip(self.alpha[j],L,H)
                
                self.alpha[i] = self.alpha[i] + self.y[i]*self.y[j]*(alpha_jo-self.alpha[j])
                
                # Find intercept
                b1 = self.b - e_i - self.y[i] * (self.alpha[i] - alpha_jo) * self.K[i, i] - \
                     self.y[j] * (self.alpha[j] - alpha_jo) * self.K[i, j]
                b2 = self.b - e_j - self.y[j] * (self.alpha[j] - alpha_jo) * self.K[j, j] - \
                     self.y[i] * (self.alpha[i] - alpha_io) * self.K[i, j]
                     
                if 0 < self.alpha[i] < self.C:
                    self.b = b1
                elif 0 < self.alpha[j] < self.C:
                    self.b = b2
                else:
                    self.b = 0.5 * (b1 + b2)
                    
            # checking for convergence
            diff = np.linalg.norm(self.alpha-alpha_prev)
            
            if (diff<self.tol):
                break
        
        print('Convergence reached after {} iterations'.format(iters))
        
        # updating support vector index
        self.sv_idx = np.where(self.alpha > 0 )[0]
                
    
    def _predict_row(self,x):
        
        '''
        k_v : is no_of_support_vectors*1 array formed after dot product of test(t) vector with all
              train_set_support_vectors
            
        '''
        k_v = self.kernel(self.x[self.sv_idx],x)
        
        ''' 
        1st arg of np.dot() does the element wise multiplication of alpha with y
        2nd arg of np.dot() is explained above 
        
        np.dot() does the element wise multiplication of (alpha,y)i[->m] with (k_v)i[->m] 
        and sums them.
        '''        
        return np.dot((self.alpha[self.sv_idx] * self.y[self.sv_idx]).T , k_v.T) + self.b
    
    def _predict(self,x=None):
        n = x.shape[0]
        result = np.zeros(n)
        
        for i in range(n):
            result[i] = np.sign(self._predict(x[i,:]))
        
        return result
    
    
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
    
    def _error(self,i):
        ''' Error for single example '''
        return self._predict_row(self.x[i]) - self.y[i]
        