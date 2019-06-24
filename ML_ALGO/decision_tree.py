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