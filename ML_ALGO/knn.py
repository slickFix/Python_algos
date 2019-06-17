#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:03:08 2019

@author: siddharth
"""

from collections import Counter

import numpy as np
from scipy.spatial.distance import euclidean

from base_estimator import BaseEstimator

class KNNBase(BaseEstimator):
    
    def __init__(self,k=5,distance_func = euclidean):
        
        '''
        Base class for k nearest neighbours classifier and regressor
        
        Parameters:-
        
        k: int default 5
            The number of neighbours to take into account. If 0, all the training examples are used.
        
        distance_func: function, default euclidean distance
            A distance function taking two arguments. Any function from scipy.spatial.distance will do
            
        '''
        
        self.k = None if k==0 else k  # lis[:None] returns the whole list
        self.distance = distance_func
        
    def aggregate(self,neighbours_targets):
        raise NotImplementedError()
        
    def _predict(self,x=None):
        
        predictions = [self._predict_x(x_val) for x_val in x]
        
        return np.array(predictions)
    
    def _predict_x(self,x):
        ''' 
        Predicts the label of a single instance x
        '''
        
        # compute the distance between x and all the examples in the training set.
        
        distances = (self.distance_func(example,x) for example in self.x)
        
        # sort all the examples by their distance to x and keep their target value
        neighbours = sorted(((distance,target) for (distance,target) in zip(distances,self.y)),key = lambda x : x[0])
        
        # Get the targets of the k-nn and aggregate them (most common one or average)
        neighbours_targets = [ target for (_,target) in neighbours[:self.k]]
        
        return self.aggregate(neighbours_targets)
    
class KNNClassifier(KNNBase):
    
    '''
    Nearest neigbors classfier
    '''
    
    def aggregate(self,neighbours_targets):
        ''' 
        Return the most common target labesl
        '''
        
        most_common_label = Counter(neighbours_targets).most_common(1)[0][0]
        return most_common_label
    
    
    
class KNNRegressor(KNNBase):
    
    '''
    Nearest neigbors regressor
    '''
    
    def aggregate(self,neighbours_targets):
        '''
        Return the mean of all the targets
        '''
        
        return np.mean(neighbours_targets)