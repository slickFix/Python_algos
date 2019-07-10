#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 22:58:36 2019

@author: siddharth
"""

import numpy as np
import scipy.spatial.distance  as dist


''' Defining vararious types of kernels for svm '''

class Linear:
    
    def __call__(self,x,y):
        return np.dot(x,y.T)
    
    def __repr__(self):
        return 'Linear Kernel'

