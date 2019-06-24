#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:41:55 2019

@author: siddharth
"""

import numpy as np

def split_target(x,y,value):
    
    left_mask = x<value
    right_mask = x >= value
    
    return y[left_mask],y[right_mask]


