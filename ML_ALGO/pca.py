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
        
        

