#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:41:55 2019

@author: siddharth
"""

import numpy as np

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
    getting split mask for a particular column
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