#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:36:21 2019

@author: siddharth
"""

import random
import numpy as np
from scipy import stats


from base_estimator import BaseEstimator

from ensemble_utils import split_dataset, split_target


random.seed(111)

class Tree():
    
    ''' Recursive implementation of decision tree '''
    
    def __init__(self,regression=False,criterion = None):
        
        # tree attributes
        self.regression = regression
        self.criterion = criterion
        self.impurity = None
        self.threshold = None
        self.column_index = None
        self.outcome = None
        self.loss = None
        
        self.left_child = None
        self.right_child = None
        
    # used to create read only attributes
    @property
    def is_terminal(self):
        return not bool(self.left_child and self.right_child)
    
    
    
    def _find_best_split(self,x,target,n_features):
        '''
        Finding the best feature and value for the split
        '''
        
        # sampling random subset of features
        subset = random.sample(list(range(0,x.shape[1])),n_features)
        
        max_gain,max_col,max_val = None,None,None
        
        for column in subset:
            
            # Column is integer or string type ??
            try:
                # if the column contains string then it throws error
                x[:column] = x[:,column].astype(float)
                
                split_values = self._find_splits(x[:,column])
            except:
                
                # if the column has only categorical(string) values
                split_values = x[:,column].unique()
            
            for value in split_values:
                if self.loss is None:
                    
                    #random forest
                    splits = split_target(x[:,column],target['y'],value)
                    gain = self.criterion(target['y'],splits)
                    
                else:
                    
                    # gradient boosting
                    left,right  = split_dataset(x,target,column,value,return_x=False)
                    gain = xgb_criterion(target,left,right,self.loss)
                    
                if (max_gain is None) or (gain > max_gain):
                    max_col, max_val, max_gain = column,value,gain
                    
        return max_col,max_val,max_gain