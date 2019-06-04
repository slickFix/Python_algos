#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:02:15 2019

@author: siddharth
"""

import logging

import autograd.numpy as np
import autograd as grad

from base_estimator import BaseEstimator
from metrics.metrics import mean_squared_error,binary_crossentropy

np.random.seed(2019)


class BasicRegression_Wrapper(BaseEstimator):
    
    ''' 
    Wrapper class for linear and logistic regression.
    '''
    def __init__(self,lr=0.001,penalty=None,C=0.01,error_tolerance=0.0001,max_iters = 1000):
        '''
        Trains regression models with gradient descent opitmizers and loss function
        depending upon the type of regression
        
        parameters:
        lr : float, default 0.001
            Learning rate.
        penalty : str, {'l1', 'l2', None'}, default None
            Regularization function name.
        C : float, default 0.01
            The regularization coefficient.
        tolerance : float, default 0.0001
            If the gradient descent updates are smaller than `tolerance`, then
            stop optimization process.
        max_iters : int, default 10000
            The maximum number of iterations.
        '''
        self.lr = lr
        self.penalty = penalty
        self.C = C
        self.error_tolerance = error_tolerance
        self.max_iters = max_iters
        self.errors = []
        self.theta = []
        self.n_samples,self.n_features = None,None
        self.cost_func = None
        
    
        
        
        