#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:25:03 2019

@author: siddharth
"""

import numpy as np
from base_estimator import BaseEstimator
from decision_tree import Decision_tree
from ensemble_utils import mse_criterion,information_gain

class Random_forest(BaseEstimator):
    '''
    Base class for random forest algorithm
    '''
    def __init__(self,max_features =None,criterion=None,max_depth = None,min_samples_split = 10,n_estimators = 10):
        '''
        Parameters
        ----------------------    
        
        max_features : int
            The number of features (columns) to consider to look for best split
        
        criterion : str
            The function to measure the quality of split (mse for regressor and info_gain for classification)
            
        max_depth : int 
            Maximum depth upto which each individual decision tree goes
        
        min_samples_split : int
            The minimum number of samples required to split internal node
        
        n_estimator : int
            The number of decision tree in the forest
            
        '''
        
        self.max_features = max_features
        self.criterion = criterion
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.d_tree = []
        
    def fit(self,x,y=None):
        self._setup_input(x,y)
        
        if self.max_features is None :
            self.max_features = int(np.sqrt(x.shape[1]))
        else:
            assert self.max_features < x.shape[1]
        
        self._train()
    
    def train(self):
        
        for tree in self.d_tree:
            tree.train(self.x,self.y,max_features = self.max_features,max_depth = self.max_depth,min_samples_split = self.min_samples_split)
            
    def predict(self,x=None):
        
        raise NotImplementedError()
        
    
        