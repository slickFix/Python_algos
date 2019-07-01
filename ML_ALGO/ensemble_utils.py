#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:41:55 2019

@author: siddharth
"""

import numpy as np

from scipy import stats


def calc_entropy(p):
    
    # converts values to probability
    p = np.bincount(p)/float(p.shape[0])
    
    # neglects 0 probabily
    ent = stats.entropy(p)
    
    if ent == -float('inf'):
        return 0.0
    
    return ent


def mse_criterion(y,splits):
    
    ''' find the mse score of the split '''
    y_mean = np.mean(y)
    
    # we are taking sum not mean of squarred errors as we finally normalize it with prob factor
    # there should be only one normalising factor i.e. either mean or prob factor not both
    
    return sum([ np.sum((split-y_mean)**2) * float(split.shape[0]/y.shape[0]) for split in splits])

def information_gain(y,splits):
    # Summation of entropy of each split node
    splits_entropy = sum([calc_entropy(split) * (float(split.shape[0])/y.shape[0]) for split in splits])
    
    return calc_entropy(y) - splits_entropy


def xgb_criterion(y,left,right,loss):
    ''' used by decision_tree which is used by gradient boosting class '''
    
    left = loss.gain(left['actual'],left['y_pred'])
    right = loss.gain(right['actual'],right['y_pred'])
    initial = loss.gain(y['actual'],y['y_pred'])
    
    gain = left+right -initial
    
    return gain


def split_target(x,y,value):
    ''' Random forest uses split_target'''
    
    # for numerical value
    if value.dtype == float: 
        left_mask = x<value
        right_mask = x >= value
    
    # for categorical values
    else :
        left_mask = (x != value)
        right_mask = (x == value)
    
    return y[left_mask],y[right_mask]


def get_split_mask(x,column,value):
    '''
    getting split mask for a particular column used by split_dataset by XGB
    '''
    
    # for numerical value
    if value.dtype == float:
        left_mask = x[:,column]<value
        right_mask = x[:,column]>=value
    
    # for categorical values
    else:
        left_mask = x[:,column] != value
        right_mask = x[:,column] == value
        
    return left_mask,right_mask

def split_dataset(x,target,column,value,return_x=True):
    
    '''
    gradient boosting uses split_dataset
    '''
    
    left_mask , right_mask = get_split_mask(x,column,value)
    
    left,right = {},{}
    
    # target is the 'y' in a dictonary form
    for key in target.keys():
        left[key] = target[key][left_mask]
        right[key] = target[key][right_mask]
        
    if return_x:
        return x[left_mask],x[right_mask],left,right
    else:
        return left,right