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

from ensemble_utils import split_dataset, split_target,xgb_criterion


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
    
    def _find_splits(self,x):
        ''' Finding all possible splits for numerical column '''
        split_values = set()
        
        # getting all the uninque values
        unique = list(np.unique(x))
        
        for i in range(1,len(unique)):
            avg = (unique[i]+unique[i-1])/2.0
            split_values.add(avg)
            
        return list(split_values)
    
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
    
    
    def train(self,x,target,max_features = None,min_samples_split = 10,max_depth=None,minimum_gain=0.01,loss=None):
        
        """Build decision tree from the training set.
        
        Parameters:
        --------------------------------------------
        
        x: array-like 
            Feature dataset.
        
        target: dictionary or array-like 
            target values.
            
        max_features: int or None
            The number of features to look for when considering the best split.
            
        min_samples_split: int
            The minimum number of samples required to split an internal node.
            
        max_depth: int 
            Maximum depth of the tree.
            
        minimum_gain: float, default 0.01
            Minimum gain required for splitting.
        
        loss: function, default None
            Loss function for gradient boosting.
            
        """
        
        if not isinstance(target,dict):
            target  =  {'y':target}
            
        # Loss for gradient boosting
        if loss is not None:
            self.loss = loss
            
        try:
            
            # Exit condition for the decision tree
            assert (x.shape[0] > min_samples_split)
            assert (max_depth>0)
            
            if max_features is None:
                max_features = x.shape[1] 
                
            column,value,gain = self._find_best_split(x,target,max_features)
            
            assert gain is not None
            
            if self.regression:
                assert (gain != 0)        
            else:
                assert (gain > minimum_gain)                
            
            self.column_index = column
            self.threshold = value
            self.impurity = gain
            
            # splitting the datset
            left_x,right_x,left_target,right_target = split_dataset(x,target,column,value)
            
            # grow left and right child
            
            self.left_child = Tree(self.regression,self.criterion)
            self.left_child.train(left_x,left_target,max_features,min_samples_split,max_depth-1,minimum_gain,loss)
            
            self.right_child = Tree(self.regression,self.criterion)
            self.right_child.train(right_x,right_target,max_features,min_samples_split,max_depth-1,minimum_gain,loss)
            
        except AssertionError:
            self._calculate_leaf_value(target)
            
    def _calculate_leaf_value(self,target):
        ''' Find optimal value for leaf '''
        
        # For gradient boosting 
        if self.loss is not None:
            self.outcome = self.loss.approximate(target['actual'],target['y_pred'])
        
        # For random forest
        else:
            if self.regression:
                # mean value for regression task
                self.outcome= np.mean(target['y'])
                
            else:
                # Probability for classification task
                self.outcome = stats.itemfreq(target['y'])[:,1]/float(target['y'].shape[0])
                
    
            