#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:44:57 2019

@author: siddharth
"""

from scipy.linalg import svd
import numpy as np
import logging

from base_estimator import BaseEstimator

class PCA(BaseEstimator):
    
    y_required = False
    
    def __init__(self,n_components,solver='svd'):
        
        ''' 
        Principal Component Analysis (PCA) implementation.
        
        Transforms a dataset of possibly correralted values into 'n' linearly 
        uncorrelated componenets. The components are ordered such that the first 
        has the largest possible variance and each following component has the 
        largest possible variance given the previous components. This causes the 
        early components to contain most of the variability in the dataset.
        
        Parameters:
        
        n_components: int
        solver : str,default 'svd'  {'svd','eigen'}
        '''
        
        self.solver = solver
        self.n_components = n_components
        self.components = None
        self.mean = None
        
    def fit(self,x,y=None):
        self.mean = np.mean(x,axis=0)
        self._decompose(x)
        
    
    def _decompose(self,x):
        
        # mean centering
        x = x.copy() # so that this copy of x doesn't alter any other x
        x -= self.mean
        
        if self.solver == 'svd':
            _,s,Vh = svd(x,full_matrices=True)
        
        elif self.solver == 'eigen':
            s,Vh = np.linalg.eig(np.cov(x.T))
            Vh = Vh.T
            
        s_squared = s ** 2
        variance_ratio = s_squared/(s_squared).sum()
        logging.info('Explained variance ratio: %s' % (variance_ratio[0:self.n_components] ))
        self.components = Vh[0:self.n_components]
        
    def transform(self,x):
        x = x.copy()
        x-= self.mean
        
        return  np.dot(x,self.components.T)
    
    def _predict(self,x=None):
        
        return self.transform(x)

