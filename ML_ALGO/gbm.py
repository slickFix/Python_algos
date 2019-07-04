#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:29:22 2019

@author: siddharth
"""

import numpy as np

from base_estimator import BaseEstimator
from ensemble_utils import mse_criterion
from decision_tree import Decision_tree

# logistic function
from scipy.special import expit

class Loss:
    ''' Base class for loss function'''
    
    def __init__(self,regularization=1.0):
        self.regularization = regularization
        
    
    def grad(self,predicted,actual):
        '''First order gradient. '''
        
        raise NotImplementedError()
        
    def hess(self,predicted,actual):
        '''Second order gradient. '''
        
        raise NotImplementedError()
    
    def approximate(self,predicted,actual):
        ''' Approximate a leaf value '''
        
        return self.grad(predicted,actual).sum() / (self.hess(predicted,actual).sum()+ self.regularization)
    
    def transform(self,pred):
        ''' Transform the prediction values. '''
        
        return pred
    
    def gain(self,predicted,actual):
        ''' Calculate the gain for each of the splits for the search '''
        
        numerator = self.grad(predicted,actual).sum() ** 2
        denominator = (self.hess(predicted,actual).sum() + self.regularization)
        
        return 0.5 * (numerator/denominator)
        
