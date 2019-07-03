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
        
class Random_forest_classifier(Random_forest):
    
    def __init__(self,n_estimators=10,max_features=None,max_depth = None,min_samples_split=10,criterion = 'entropy'):
        
        super(Random_forest_classifier,self).__init__(max_features =max_features,criterion=criterion,
             max_depth = max_depth,min_samples_split = min_samples_split,
             n_estimators = n_estimators)
        
        if criterion == 'entropy':
            self.criterion = information_gain
        else:
            raise ValueError()
            
        # Initializing empty trees
        for _ in range(n_estimators):
            self.d_tree.append(Decision_tree(criterion=self.criterion))
        
    def _predict(self,x=None):
        
        n_classes = np.unique(self.y).shape[0]
        
        predictions = np.zeros(x.shape[0],n_classes)
        
        for row in range(x.shape[0]):
            row_pred = np.zeros(n_classes)
            
            for tree in self.d_tree:
                row_pred+= tree.predict_row(x[row,:])
                
            row_pred /= self.n_estimators
            predictions[row,:] = row_pred
        return predictions

class Random_forest_Regressor(Random_forest):
    
    def __init__(self,n_estimators=10,max_features=None,max_depth = None,min_samples_split=10,criterion = 'mse'):
        
        super(Random_forest_Regressor,self).__init__(max_features =max_features,criterion=criterion,
             max_depth = max_depth,min_samples_split = min_samples_split,
             n_estimators = n_estimators)
        
        if criterion == 'mse':
            self.criterion = mse_criterion
        else:
            raise ValueError()
        
        # Initializing empyt trees
        for _ in range(self.n_estimators):
            self.d_tree.append(Decision_tree(criterion=self.criterion,regression=True))
            
    
        